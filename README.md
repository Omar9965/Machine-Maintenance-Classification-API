# 🛠️ Machine Predictive Maintenance Classification API

A **FastAPI service** for **predicting machine failure** using classification models, feature engineering, and robust preprocessing for reliable predictive maintenance decision support.

---

## 📌 Table of Contents

* Project Overview
* Features
* Project Structure
* Installation
* Usage
* API Endpoints
* Example Request
* Notes
* Future Improvements

---

## 🚀 Project Overview

Predictive maintenance reduces unplanned downtime by anticipating failures before they happen. This API uses **FastAPI** and **XGBoost** to predict machine failure from sensor and operational data.

Key components:
✅ Feature engineering
✅ Preprocessing pipelines (scaling, encoding)
✅ Tuned thresholds for classification
✅ Real-time API for model inference
✅ Pydantic validation of requests
✅ Docker-ready for consistent deployment

---

## ✨ Features

* **Structured pipeline** for robust preprocessing and consistent feature engineering.
* **Pydantic validation** ensuring clean, typed, constrained input.
* **FastAPI REST endpoints** for real-time predictions.
* **Dockerized** for easy deployment on any environment.

---

## 🗂️ Project Structure

```
Machine Predictive Maintenance Classification/
│
├── Data/
│   └── ai4i2020.csv             # Dataset
│
├── Models/
│   ├── preprocessor.pkl         # Preprocessing pipeline
│   └── xgb_model.pkl            # Trained XGBoost model
│
├── Notebook/
│   └── model.ipynb              # EDA/Training notebook
│
├── utils/
│   ├── config.py                # Load models and config
│   ├── inference.py             # Prediction logic
│   ├── feature_engineering.py   # Adds engineered features
│   └── MachineData.py           # Pydantic schema for validation
│
├── main.py                      # FastAPI entry point
├── requirements.txt             # Python dependencies
├── docker-compose.yaml          # Docker orchestration
├── Dockerfile                   # Docker build instructions
├── .env                         # Environment variables (local)
├── env.example                  # Example environment file
└── README.md                    # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/Omar9965/Machine-Maintenance-Classification-API
cd "Machine Predictive Maintenance Classification"
```

### 2️⃣ (Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 4️⃣ Add environment variables:

Copy `env.example` to `.env` and edit if needed:

```bash
cp env.example .env
```

---

## ▶️ Usage

### 🚀 **Running without Docker:**

```bash
uvicorn main:app --reload
```

Access the API:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 🚀 **Running with Docker (Recommended for consistency):**

1️⃣ **Build the image:**

```bash
docker-compose build
```

2️⃣ **Run the containers:**

```bash
docker-compose up
```

Access:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📡 API Endpoints

### 1️⃣ `GET /`

Health check to confirm API is live.

### 2️⃣ `POST /predict/xgboost`

Accepts JSON matching the `MachineData` schema, applies preprocessing and feature engineering, and returns:

* `Failure_prediction`: True/False
* `Failure_probability`: Float (probability of failure)

---

## 📝 Example Request

### Request:

```json
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
```

### Response:

```json
{
    "Failure_prediction": false,
    "Failure_probability": 0.123456
}
```

---

# Machine Predictive Maintenance Classification API
