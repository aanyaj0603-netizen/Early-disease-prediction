<img width="1487" height="1012" alt="Screenshot 2026-10-01 151703" src="https://github.com/user-attachments/assets/7bb1bf9e-28ab-4ef1-bd6d-997ca78cabb5" />
<img width="1497" height="1015" alt="Screenshot 2026-10-01 151523" src="https://github.com/user-attachments/assets/0c9c9eb9-c979-4d3b-b7b1-58ad94a2e61c" />
# Health Signals: Product Requirements

## Purpose
A polished HCLTech concept experience that lets users explore symptom-based disease classification using a machine-learning model. It is an educational demo, not an early-detection or clinical product.

## Users and Core Flow
1. A user searches and selects one or more symptoms from the model's vocabulary.
2. The page sends selected symptom indicators to a local Flask API.
3. The API returns the closest disease label and the top three model matches.
4. The page explains the result and its limitations without storing the selection.

## Data and Model
- Dataset: [Kaggle Disease Prediction Using Machine Learning](https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning).
- Local data: `data/Training.csv` and `data/Testing.csv`.
- Inputs: 132 binary symptom features. Targets: 41 disease labels in the downloaded files.
- Current baseline: scikit-learn 5-nearest-neighbors, trained from `Training.csv` at app startup.
- Reported test accuracy: 100% (42 of 42 rows in `Testing.csv`). This small dataset result should not be presented as evidence of real-world or clinical accuracy.
- Result percentages represent the share of the five nearest training records voting for a label. They are not calibrated probabilities or personal risk estimates.
- The user's Colab-trained model is not connected yet. It can replace the baseline after an exported, feature-compatible model is provided.

## Requirements
- Use the dataset's symptom vocabulary and feature order; reject unknown symptoms and empty submissions.
- Serve the responsive webpage and JSON endpoints from one local Flask app.
- Do not persist submitted symptoms.
- Clearly identify the dataset, model, and test-set size/accuracy.
- Display a persistent warning that model output is not diagnosis or medical advice.

## Acceptance Criteria
- The page loads the 132 symptoms from `/api/symptoms`.
- Selecting symptoms and submitting returns a disease prediction and up to three ranked matches from `/api/predict`.
- The page displays model/test metadata and describes match scores as neighbor votes.
- Empty or invalid submissions return a readable error.
- The layout works on desktop and mobile; no symptom data is saved.

## Run Locally
```powershell
py -m pip install -r requirements.txt
py app.py
```
Open `http://127.0.0.1:5000`.

## Out of Scope
Clinical diagnosis, disease-risk prediction before symptoms, medical advice, production deployment, user accounts, and persistent patient records.
