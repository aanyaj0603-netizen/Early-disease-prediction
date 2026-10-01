import csv
import os
from pathlib import Path

import joblib
from flask import Flask, jsonify, request, send_from_directory
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


ROOT = Path(__file__).resolve().parent
TRAINING_FILE = ROOT / "data" / "Training.csv"
MODEL_PATH = os.environ.get("MODEL_PATH")
app = Flask(__name__)


def read_dataset(path):
    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        while columns and not columns[-1].strip():
            columns.pop()
        if not columns or columns[-1].lower() != "prognosis":
            raise ValueError(f"Expected a prognosis target column in {path.name}.")
        symptoms = columns[:-1]
        rows = list(reader)
    features = [[float(row[symptom] or 0) for symptom in symptoms] for row in rows]
    labels = [row["prognosis"] for row in rows]
    return symptoms, features, labels


def load_predictor():
    symptoms, features, labels = read_dataset(TRAINING_FILE)
    if MODEL_PATH:
        model = joblib.load(Path(MODEL_PATH).expanduser().resolve())
        expected = list(getattr(model, "feature_names_in_", symptoms))
        if set(expected) != set(symptoms):
            raise ValueError("The saved model features do not match Kaggle Training.csv.")
        name = "Your saved model"
    else:
        model = KNeighborsClassifier(n_neighbors=5, weights="uniform")
        model.fit(features, labels)
        expected = symptoms
        name = "Kaggle 5-nearest-neighbors"

    test_symptoms, test_features, test_labels = read_dataset(ROOT / "data" / "Testing.csv")
    if set(test_symptoms) != set(expected):
        raise ValueError("Testing.csv features do not match the trained model.")
    test_indexes = {symptom: index for index, symptom in enumerate(test_symptoms)}
    aligned_test_features = [
        [row[test_indexes[symptom]] for symptom in expected]
        for row in test_features
    ]
    test_accuracy = accuracy_score(test_labels, model.predict(aligned_test_features))
    return model, expected, name, round(test_accuracy * 100, 1), len(test_labels)


model, symptom_names, model_name, test_accuracy, test_count = load_predictor()


@app.get("/")
def index():
    return send_from_directory(ROOT, "index.html")


@app.get("/api/symptoms")
def get_symptoms():
    return jsonify(
        symptoms=symptom_names,
        disease_count=len(model.classes_),
        model_name=model_name,
        test_accuracy=test_accuracy,
        test_count=test_count,
    )


@app.post("/api/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    selected = payload.get("symptoms")
    if not isinstance(selected, list) or not selected:
        return jsonify(error="Select at least one symptom to continue."), 400
    selected_set = set(selected)
    if selected_set.difference(symptom_names):
        return jsonify(error="One or more symptoms are not in the model vocabulary."), 400

    feature_vector = [[int(symptom in selected_set) for symptom in symptom_names]]
    result = {
        "prediction": str(model.predict(feature_vector)[0]).replace("_", " ").title(),
        "model_name": model_name,
        "selected_count": len(selected_set),
        "score_label": "neighbor vote" if isinstance(model, KNeighborsClassifier) else "model score",
        "score_note": (
            "Match percentages show how many of the five nearest training records voted for each label. "
            "They are not calibrated probabilities."
            if isinstance(model, KNeighborsClassifier)
            else "Match percentages are model outputs, not calibrated probabilities."
        ),
        "top_matches": [],
    }
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(feature_vector)[0]
        top_indexes = sorted(range(len(probabilities)), key=probabilities.__getitem__, reverse=True)[:3]
        result["top_matches"] = [
            {
                "disease": str(model.classes_[index]).replace("_", " ").title(),
                "score": round(float(probabilities[index]) * 100, 1),
            }
            for index in top_indexes
        ]
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=False)