# PRD --- HealthGuard AI

## AI-Based Early Disease Prediction & Risk Assessment Platform

**Target Organization:** HCLTech\
**Product Type:** Healthcare AI / Predictive Analytics\
**Primary Users:** Doctors, healthcare professionals, hospitals,
diagnostic centers, and patients with a restricted view

------------------------------------------------------------------------

## 1. Product Vision

HealthGuard AI is an AI-powered healthcare decision-support platform
that analyzes patient health information and identifies patterns
associated with elevated risk for selected diseases.

The platform is designed to support earlier clinical evaluation and
preventive action by providing risk estimates, contributing factors, and
explainable AI insights.

> **Important:** The system provides risk estimation and decision
> support, not a medical diagnosis. Final diagnosis and treatment
> decisions remain with qualified healthcare professionals.

------------------------------------------------------------------------

## 2. Problem Statement

Many diseases are detected only after symptoms become significant.
Healthcare organizations collect large amounts of patient information,
including demographic data, vital signs, laboratory results, medical
history, and lifestyle information.

This data can be difficult to analyze manually at scale.

HealthGuard AI will use machine learning and explainable AI to analyze
relevant patient information and generate an understandable disease-risk
assessment for healthcare professionals.

------------------------------------------------------------------------

## 3. Product Objectives

### Primary Objectives

-   Predict the estimated risk of selected diseases at an early stage.
-   Identify important factors contributing to each prediction.
-   Provide interpretable AI results.
-   Support healthcare professionals in prioritizing patients for
    further evaluation.
-   Reduce manual analysis of large healthcare datasets.
-   Maintain strong privacy and security for healthcare information.

### Secondary Objectives

-   Provide healthcare dashboards.
-   Track prediction history.
-   Support multiple disease-specific models.
-   Monitor model performance and data drift.
-   Provide auditable prediction records.

------------------------------------------------------------------------

## 4. Initial Disease Scope

The MVP should focus on a limited number of diseases rather than
attempting to predict every disease.

### Recommended MVP

1.  Diabetes
2.  Cardiovascular disease

### Future Expansion

-   Chronic kidney disease
-   Liver disease
-   Other conditions based on validated datasets and clinical
    requirements

### Example Input Data

  -----------------------------------------------------------------------
  Disease                             Example Features
  ----------------------------------- -----------------------------------
  Diabetes                            Glucose, BMI, age, blood pressure,
                                      pregnancies, insulin

  Cardiovascular Disease              Age, blood pressure, cholesterol,
                                      smoking status, BMI, heart rate

  Kidney Disease                      Creatinine, blood urea, blood
                                      pressure, hemoglobin, glucose

  Liver Disease                       Bilirubin, liver enzymes, albumin,
                                      age, sex
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 5. Target Users

### 5.1 Doctor / Healthcare Professional

The doctor can:

-   Register or select a patient.
-   Enter or import patient health data.
-   Generate a disease-risk assessment.
-   View contributing risk factors.
-   Review model explanations.
-   View prediction history.
-   Export a patient risk report.

### 5.2 Hospital Administrator

The administrator can:

-   Monitor prediction statistics.
-   Manage users and roles.
-   Monitor system performance.
-   Monitor model performance.
-   Review audit logs.

### 5.3 Patient

The patient-facing interface should provide only an appropriate,
restricted view:

-   Risk assessment.
-   General preventive information.
-   Recommendation to consult a healthcare professional.

The patient interface should not present a prediction as a confirmed
diagnosis.

------------------------------------------------------------------------

## 6. Core Features

### 6.1 Patient Registration

Patient information may include:

-   Patient ID
-   Age
-   Sex
-   Relevant demographic information
-   Medical history
-   Existing conditions

### 6.2 Health Data Input

#### Demographics

-   Age
-   Sex

#### Vital Signs

-   Blood pressure
-   Heart rate
-   BMI
-   Other relevant measurements

#### Laboratory Results

-   Glucose
-   Cholesterol
-   Creatinine
-   Hemoglobin
-   Liver enzymes
-   Other disease-specific biomarkers

#### Lifestyle Information

-   Smoking status
-   Physical activity
-   Other relevant lifestyle factors

#### Medical History

-   Family history
-   Existing conditions
-   Previous diagnoses

------------------------------------------------------------------------

## 7. AI Prediction Engine

The prediction engine processes patient information and sends the
relevant features to the appropriate disease-specific model.

### Example

**Input:**

``` text
Age = 52
BMI = 29.4
Glucose = 145
Blood Pressure = 148/92
Family History = Yes
```

**Example Output:**

``` text
Condition: Diabetes
Estimated Risk Probability: 78%
Risk Category: Elevated
```

The result must be clearly presented as a risk estimate rather than a
confirmed diagnosis.

------------------------------------------------------------------------

## 8. Machine Learning Pipeline

``` text
Patient Data
     ↓
Data Validation
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
ML Model
     ↓
Risk Probability
     ↓
Risk Categorization
     ↓
Explainable AI
     ↓
Healthcare Dashboard
```

### Candidate Algorithms

-   Logistic Regression
-   Decision Tree
-   Random Forest
-   XGBoost
-   LightGBM
-   CatBoost

Multiple models should be evaluated during development. The final model
should be selected using appropriate validation metrics and
clinical/product requirements rather than accuracy alone.

------------------------------------------------------------------------

## 9. Data Preprocessing

The preprocessing pipeline should include:

``` text
Raw Dataset
     ↓
Missing Value Detection
     ↓
Duplicate Removal
     ↓
Outlier Analysis
     ↓
Data Type Correction
     ↓
Categorical Encoding
     ↓
Feature Scaling
     ↓
Feature Engineering
     ↓
Train/Test Split
```

### Data Quality Requirements

-   Handle missing values appropriately.
-   Detect duplicate records.
-   Validate data types and ranges.
-   Investigate outliers.
-   Encode categorical variables.
-   Prevent data leakage.
-   Apply preprocessing consistently during training and inference.

------------------------------------------------------------------------

## 10. Feature Engineering

Potential features may include:

-   BMI category
-   Age groups
-   Pulse pressure
-   Relevant ratios
-   Aggregated clinical indicators
-   Disease-specific derived features

Feature engineering should be supported by domain reasoning and
validated experimentally.

------------------------------------------------------------------------

## 11. Explainable AI

Explainability is a major component of the product.

Instead of displaying only:

> High Risk

the system should show the major factors contributing to the prediction.

### Example

``` text
Prediction: Elevated Risk

Major Contributing Factors

Glucose          ██████████
BMI              ███████
Age              ██████
Blood Pressure   █████
Family History   ████
```

### Technology

Use **SHAP (SHapley Additive exPlanations)** to provide feature-level
explanations.

### Explanation Flow

``` text
Prediction
    ↓
SHAP
    ↓
Feature Contribution
    ↓
Human-Readable Explanation
```

------------------------------------------------------------------------

## 12. Risk Categories

The application can display risk categories based on validated model
thresholds.

Example interface:

  Example Score Range   Display
  --------------------- -------------------------
  0--30%                Lower Estimated Risk
  30--60%               Moderate Estimated Risk
  60--80%               Elevated Estimated Risk
  80--100%              Higher Estimated Risk

These ranges are examples for product design and must not be treated as
universal clinical thresholds. Final thresholds should be validated for
the specific model and intended use.

------------------------------------------------------------------------

## 13. Dashboard

The main dashboard should display:

``` text
------------------------------------------------
                 HEALTHGUARD AI
------------------------------------------------

Patients Analyzed        12,458

Lower Risk               7,842
Moderate Risk            2,951
Elevated Risk            1,665

------------------------------------------------
Disease Risk Distribution
------------------------------------------------

Diabetes                 ███████████
Cardiovascular           ████████
Kidney                   ████
Liver                     ███

------------------------------------------------
Recent Assessments
------------------------------------------------

Patient ID | Condition | Risk | Date
------------------------------------------------
P1023      | Diabetes  | 72%  | 30 Sep
P1045      | Cardio    | 64%  | 30 Sep
P1087      | Diabetes  | 31%  | 29 Sep
```

The numerical values above are UI examples and should be replaced with
actual system data.

------------------------------------------------------------------------

## 14. Patient Risk Assessment Page

Example interface:

``` text
Patient: P1023
Age: 52
Sex: Female

--------------------------------
DIABETES RISK ASSESSMENT
--------------------------------

Estimated Risk: 72%
Category: Elevated

Key Factors:

✓ Elevated glucose
✓ BMI
✓ Blood pressure
✓ Family history

--------------------------------
MODEL EXPLANATION

Glucose       +0.32
BMI           +0.17
Age           +0.11
BP            +0.08

--------------------------------

Recommended next step:
Clinical evaluation and appropriate
diagnostic testing as determined by
a healthcare professional.
```

------------------------------------------------------------------------

## 15. Technology Stack

### Frontend

-   React.js
-   HTML
-   CSS
-   JavaScript
-   Charting library such as Recharts or Chart.js

### Backend

-   Python
-   FastAPI
-   REST APIs

### Machine Learning

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   XGBoost / CatBoost
-   SHAP

### Database

-   PostgreSQL

### Deployment

Potential enterprise deployment options:

-   Docker
-   Cloud infrastructure
-   CI/CD pipeline
-   Secure API gateway

------------------------------------------------------------------------

## 16. Database Design

Suggested tables:

``` text
Users
Patients
MedicalRecords
LabResults
Predictions
ModelVersions
AuditLogs
```

### Example Relationships

``` text
User
  ↓
Patient
  ↓
Medical Record
  ↓
Prediction
  ↓
Model Version
```

------------------------------------------------------------------------

## 17. System Architecture

``` text
                 ┌─────────────────┐
                 │    React UI     │
                 └────────┬────────┘
                          │
                          ↓
                 ┌─────────────────┐
                 │    FastAPI      │
                 │    Backend      │
                 └────────┬────────┘
                          │
             ┌────────────┼────────────┐
             ↓            ↓            ↓
        PostgreSQL     ML Service    Auth
             │            │
             │            ↓
             │       ┌───────────┐
             │       │ ML Models │
             │       └─────┬─────┘
             │             ↓
             │           SHAP
             │             │
             └─────────────┼──────────
                           ↓
                    Risk Assessment
```

------------------------------------------------------------------------

## 18. API Requirements

### Patient API

``` text
POST /api/patients
GET /api/patients/{patient_id}
PUT /api/patients/{patient_id}
```

### Prediction API

``` text
POST /api/predict/diabetes
POST /api/predict/cardiovascular
GET /api/predictions/{patient_id}
```

### Model API

``` text
GET /api/models
GET /api/models/{model_id}
```

### Authentication API

``` text
POST /api/auth/login
POST /api/auth/logout
```

------------------------------------------------------------------------

## 19. Security Requirements

Healthcare data requires strong security controls.

The system should include:

-   Authentication
-   Role-based access control
-   Encryption in transit
-   Encryption at rest
-   Secure API authentication
-   Input validation
-   Session management
-   Audit logs
-   Access logging
-   Data minimization
-   Secure secrets management

The deployed solution should also be mapped to applicable healthcare
privacy, security, and regulatory requirements for its intended
geography and organization.

------------------------------------------------------------------------

## 20. AI Safety Requirements

The system should:

-   Clearly distinguish risk prediction from diagnosis.
-   Display model limitations.
-   Avoid unsupported medical recommendations.
-   Display model/version information.
-   Log predictions for auditing.
-   Monitor model drift.
-   Monitor performance across relevant patient groups.
-   Require professional review for clinical decisions.

------------------------------------------------------------------------

## 21. Model Evaluation

Model evaluation should include:

-   Accuracy
-   Precision
-   Recall / Sensitivity
-   Specificity
-   F1-score
-   ROC-AUC
-   PR-AUC
-   Confusion Matrix
-   Calibration

For an early-risk screening application, false negatives are
particularly important, so sensitivity should be evaluated alongside
specificity and calibration.

### Model Comparison Template

  Model                   Accuracy   Recall    F1   ROC-AUC
  --------------------- ---------- -------- ----- ---------
  Logistic Regression          ---      ---   ---       ---
  Random Forest                ---      ---   ---       ---
  XGBoost                      ---      ---   ---       ---
  CatBoost                     ---      ---   ---       ---

Actual values should be filled using the project's validation results.

------------------------------------------------------------------------

## 22. Model Monitoring

After deployment:

``` text
Production Data
      ↓
Prediction Monitoring
      ↓
Performance Monitoring
      ↓
Data Drift Detection
      ↓
Model Retraining
```

Track:

-   Prediction distribution
-   Data drift
-   Missing-value changes
-   Feature distribution changes
-   Recall
-   Precision
-   False-positive rate
-   False-negative rate
-   Calibration

------------------------------------------------------------------------

## 23. Functional Requirements

### FR-01: User Authentication

The system shall allow authorized users to securely log in.

### FR-02: Patient Management

The system shall allow authorized healthcare professionals to create and
manage patient records.

### FR-03: Health Data Entry

The system shall allow authorized users to enter relevant health and
laboratory information.

### FR-04: Disease Prediction

The system shall generate disease-specific risk estimates using trained
ML models.

### FR-05: Explainability

The system shall display major factors contributing to the prediction.

### FR-06: Prediction History

The system shall maintain a history of predictions associated with a
patient.

### FR-07: Reporting

The system shall allow authorized users to generate patient risk
reports.

### FR-08: Model Management

The system shall maintain model versions and associated metadata.

### FR-09: Audit Logging

The system shall record important user and prediction-related actions.

------------------------------------------------------------------------

## 24. Non-Functional Requirements

### Performance

-   Prediction API should return results within an acceptable response
    time.
-   Dashboard pages should load efficiently.

### Scalability

The architecture should support adding additional disease models without
redesigning the entire platform.

### Security

Patient information must be protected using appropriate authentication,
authorization, encryption, and audit controls.

### Reliability

The system should handle API and model-service failures gracefully.

### Maintainability

ML models, preprocessing pipelines, APIs, and frontend components should
be modular.

### Explainability

Prediction results should be understandable to intended users.

------------------------------------------------------------------------

## 25. MVP Scope

The first version should include:

### Frontend

-   Login
-   Dashboard
-   Patient registration
-   Health-data form
-   Prediction page
-   SHAP explanation
-   Prediction history

### Backend

-   FastAPI
-   Authentication
-   Prediction APIs
-   Database integration

### ML

-   Diabetes model
-   Cardiovascular disease model
-   Preprocessing pipeline
-   Feature engineering
-   Model evaluation
-   SHAP explanations

### Reports

-   Patient risk report
-   Prediction history

------------------------------------------------------------------------

## 26. Development Phases

### Phase 1 --- Research & Requirements

-   Define diseases.
-   Identify datasets.
-   Study relevant features.
-   Define user roles.
-   Define system requirements.

### Phase 2 --- Data Engineering

-   Data collection
-   Data cleaning
-   Missing-value treatment
-   Outlier analysis
-   Feature engineering
-   Exploratory data analysis

### Phase 3 --- ML Development

-   Baseline models
-   Model comparison
-   Hyperparameter tuning
-   Cross-validation
-   Evaluation
-   Explainability

### Phase 4 --- Backend

-   FastAPI
-   Authentication
-   Database
-   Prediction APIs
-   Model serving

### Phase 5 --- Frontend

-   Login
-   Dashboard
-   Patient management
-   Prediction interface
-   Visualization
-   Reports

### Phase 6 --- Testing

-   Unit testing
-   API testing
-   Model testing
-   Security testing
-   UI testing
-   Data validation

### Phase 7 --- Deployment

-   Dockerization
-   Cloud/enterprise deployment
-   Monitoring
-   Logging
-   Model versioning

------------------------------------------------------------------------

## 27. Future Scope

### Phase 2

-   Additional diseases
-   Hospital integration
-   EHR integration
-   Automated laboratory-data ingestion
-   Doctor notification system

### Phase 3

-   Cloud deployment
-   Continuous model monitoring
-   Time-series health data
-   Wearable-device integration
-   More advanced explainability

### Phase 4

Build an enterprise healthcare AI platform capable of supporting
multiple predictive models through a common model-serving, monitoring,
and governance layer.

------------------------------------------------------------------------

## 28. Success Metrics

### Machine Learning Metrics

-   ROC-AUC
-   PR-AUC
-   Sensitivity
-   Specificity
-   F1-score
-   Calibration

### Product Metrics

-   Prediction response time
-   Successful prediction rate
-   Dashboard response time
-   Report generation time
-   User adoption

### Operational Metrics

-   Model drift
-   Data quality
-   API uptime
-   API error rate

------------------------------------------------------------------------

## 29. Key Risks and Mitigation

  -----------------------------------------------------------------------
  Risk                                Mitigation
  ----------------------------------- -----------------------------------
  Poor data quality                   Data validation and preprocessing

  Class imbalance                     Appropriate sampling and evaluation
                                      metrics

  Data leakage                        Strict train/validation/test
                                      separation

  Model bias                          Evaluate performance across
                                      relevant groups

  False negatives                     Monitor sensitivity and threshold
                                      performance

  Model drift                         Continuous monitoring

  Privacy risks                       Encryption, access control,
                                      auditing

  Over-reliance on AI                 Present output as decision support,
                                      not diagnosis

  Dataset limitations                 Document dataset provenance and
                                      limitations
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 30. One-Line Product Pitch

> **HealthGuard AI is an explainable AI-powered healthcare
> decision-support platform that analyzes patient health data to
> estimate early disease risk, identify contributing factors, and help
> healthcare professionals prioritize patients for appropriate clinical
> evaluation.**

------------------------------------------------------------------------

## 31. Recommended Project Positioning

The project should not be presented simply as:

**"Disease Prediction Using Machine Learning."**

Instead, position it as:

**Data → Preprocessing → Feature Engineering → ML → Explainable AI → API
→ Dashboard → Security → Monitoring**

This makes the project an end-to-end enterprise AI solution rather than
only an ML model.
