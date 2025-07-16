
# 🛠️ Machine Predictive Maintenance Classification API

A production-ready **FastAPI service** for **predicting machine failure** using classification models with engineered features, robust preprocessing, and tuned thresholds, ensuring reliable predictive maintenance decision support.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technical Details](#technical-details)
- [Example Request](#example-request)
- [Notes](#notes)
- [Future Improvements](#future-improvements)

---

## 🚀 Project Overview

Predictive maintenance reduces unplanned downtime by anticipating failures before they happen. This project builds a **FastAPI REST API** using **LightGBM (or XGBoost initially)** models trained on engineered sensor and operational data for **binary machine failure prediction**.

The pipeline includes:

✅ Feature engineering  
✅ Preprocessing pipelines (scaling, encoding)  
✅ Tuned thresholds for classification  
✅ Model inference API  
✅ Pydantic validation with type and value constraints  
✅ CORS for frontend integration  

---

## ✨ Features

- **Clean ML pipeline**: Scikit-learn pipelines, feature engineering, and preprocessing stored via `joblib`.
- **Model threshold tuning** using precision-recall curves for optimal F1 performance.
- **FastAPI deployment** with real-time JSON input prediction.
- **Validation** using Pydantic with constraints on sensor values.
- **Structured project** for clarity, modularity, and scalability.
- **Docker-ready architecture** (optional for your next phase).

---

## 🗂️ Project Structure

\`\`\`
Machine Predictive Maintenance Classification/
│
├── main.py                   # FastAPI entry point
├── requirements.txt          # Dependencies
├── .env                      # Environment variables
│
├── models/                   # Saved preprocessor and model
│   ├── preprocessor.pkl
│   └── xgb_model.pkl
│
├── utils/
│   ├── config.py             # Loads models and config
│   ├── inference.py          # Prediction function
│   ├── feature_engineering.py # add_engineered_features function
│   └── MachineData.py        # Pydantic schema for validation
│
└── README.md                 # Project documentation
\`\`\`

---

## ⚙️ Installation

1️⃣ Clone the repository:
\`\`\`bash
git clone <repository_url>
cd Machine Predictive Maintenance Classification
\`\`\`

2️⃣ (Recommended) Create a virtual environment:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3️⃣ Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4️⃣ Add a \`.env\` file:
\`\`\`env
APP_NAME=Machine Predictive Maintenance Classification
VERSION=1.0
\`\`\`

---

## ▶️ Usage

Run the FastAPI server:
\`\`\`bash
uvicorn main:app --reload
\`\`\`
Access the interactive Swagger UI:
\`\`\`
http://127.0.0.1:8000/docs
\`\`\`
Or the ReDoc UI:
\`\`\`
http://127.0.0.1:8000/redoc
\`\`\`

---

## 📡 API Endpoints

### 1️⃣ \`GET /\`
Health check to confirm the API is running.

### 2️⃣ \`POST /predict/xgboost\`
Accepts **JSON data** matching the \`MachineData\` schema, performs preprocessing, engineered feature addition, and returns:
- \`Failure_prediction\`: Boolean indicating if the machine is predicted to fail.
- \`Failure_probability\`: Probability of failure.

---

## 🛠️ Technical Details

✅ **Feature Engineering**:
- Handled in \`add_engineered_features\` inside \`feature_engineering.py\`.
- Called during inference to maintain consistency with training.

✅ **Preprocessing**:
- Scaling, encoding, and feature selection using scikit-learn pipeline.
- Saved and loaded using \`joblib\` for consistency across training and inference.

✅ **Model**:
- Initially used XGBoost, later switched to LightGBM for speed.
- Tuned \`scale_pos_weight\` to handle class imbalance.
- Tuned classification threshold for better F1 performance.

✅ **Pydantic Validation**:
- Enforces:
    - Type: L, M, or H
    - Temperature, torque, tool wear ranges to prevent invalid inputs.

✅ **Error Handling**:
- Clear errors when input keys mismatch.
- Detects missing features during pipeline transformation.

---

## 📝 Example Request

### Request:
\`\`\`json
POST http://127.0.0.1:8000/predict/xgboost
Content-Type: application/json
{
    "Type": "M",
    "Air temperature [K]": 300.0,
    "Process temperature [K]": 310.0,
    "Rotational speed [rpm]": 1500.0,
    "Torque [Nm]": 40.0,
    "Tool wear [min]": 10.0
}
\`\`\`

### Response:
\`\`\`json
{
  "Failure_prediction": false,
  "Failure_probability": 0.123456
}
\`\`\`

