# 🛠️ Machine Predictive Maintenance Classification

A **full-stack FastAPI application** for **predicting machine failure** using XGBoost classification, built with a scalable **MVC architecture**, feature engineering pipelines, and a modern dark-themed web UI.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Web Pages](#-web-pages)
- [Example Request](#-example-request)
- [Testing](#-testing)
- [Future Improvements](#-future-improvements)

---

## 🚀 Project Overview

Predictive maintenance reduces unplanned downtime by anticipating failures before they happen. This application uses **FastAPI** and **XGBoost** to predict machine failure from sensor and operational data.

Key components:

✅ MVC architecture with clear separation of concerns  
✅ App factory pattern for scalability and testability  
✅ Feature engineering pipeline (14 derived features)  
✅ Preprocessing pipelines (scaling, encoding)  
✅ Tuned classification threshold for precision  
✅ REST API with versioned endpoints (`/api/v1/`)  
✅ Web UI with prediction form and result visualization  
✅ Pydantic validation with type-safe configuration  
✅ Global error handling middleware  
✅ Centralized logging  
✅ Docker-ready for consistent deployment

---

## ✨ Features

- **MVC Structure** — Models, Views, Controllers, and Services are cleanly separated.
- **App Factory** — `create_app()` assembles all layers, enabling multiple configurations and easy testing.
- **Dual Interface** — REST API for programmatic access + Web UI for interactive predictions.
- **Pydantic Settings** — Type-safe, validated configuration from `.env` files with caching.
- **ModelManager** — ML model lifecycle management with lazy-load safety.
- **PredictionService** — Business logic decoupled from HTTP — reusable from API, web, or CLI.
- **Modern Web UI** — Dark glassmorphism theme with animations, responsive design, and a probability gauge.
- **Global Error Handling** — Consistent JSON error responses for API, user-friendly error display for web.
- **Dockerized** — Ready for deployment on any environment.

---

## 🏗️ Architecture

```
Client Request
  ├── API: /api/v1/predict/xgboost (JSON)
  │     └── API Controller
  └── Web: /predict (Form)
        └── Web Controller
              │
              ▼
        PredictionService (Business Logic)
              │
              ├── Feature Engineering (14 features)
              ├── Preprocessing (preprocessor.pkl)
              └── XGBoost Inference (xgb_model.pkl)
                    │
                    ▼
              PredictionResponse
              ├── Failure_prediction: bool
              └── Failure_probability: float
```

---

## 🗂️ Project Structure

```
Machine-Maintenance-Classification-API/
│
├── app/
│   ├── __init__.py                    # App factory (create_app)
│   │
│   ├── core/
│   │   ├── config.py                  # Pydantic BaseSettings
│   │   └── logging.py                 # Centralized logging
│   │
│   ├── models/                        # MODEL layer
│   │   ├── schemas.py                 # Pydantic request/response schemas
│   │   └── ml_models.py              # ModelManager (load & serve models)
│   │
│   ├── services/                      # Business logic layer
│   │   ├── prediction_service.py      # Prediction orchestration
│   │   └── feature_engineering.py     # 14 derived features
│   │
│   ├── controllers/                   # CONTROLLER layer
│   │   ├── api/
│   │   │   ├── home_controller.py     # GET /api/v1/
│   │   │   └── prediction_controller.py  # POST /api/v1/predict/xgboost
│   │   └── web/
│   │       ├── home_controller.py     # GET /
│   │       └── prediction_controller.py  # GET & POST /predict
│   │
│   ├── views/                         # VIEW layer
│   │   ├── templates/
│   │   │   ├── base.html              # Base layout with navigation
│   │   │   ├── index.html             # Landing page
│   │   │   ├── predict.html           # Prediction form
│   │   │   └── result.html            # Result with probability gauge
│   │   └── static/
│   │       ├── css/style.css          # Dark theme design system
│   │       └── js/main.js             # Client-side interactivity
│   │
│   ├── middleware/
│   │   └── error_handler.py           # Global exception handlers
│   │
│   └── routes/
│       └── router.py                  # Central route registration
│
├── Models/
│   ├── preprocessor.pkl               # Sklearn preprocessing pipeline
│   └── xgb_model.pkl                  # Trained XGBoost classifier
│
├── Data/
│   └── ai4i2020.csv                   # AI4I 2020 dataset
│
├── Notebook/
│   └── model.ipynb                    # EDA & training notebook
│
├── tests/
│   ├── conftest.py                    # Pytest fixtures
│   └── test_api.py                    # API & web endpoint tests
│
├── main.py                            # Entry point
├── requirements.txt                   # Python dependencies
├── Dockerfile                         # Docker build
├── docker-compose.yaml                # Docker orchestration
├── env.example                        # Example environment variables
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Omar9965/Machine-Maintenance-Classification-API
cd Machine-Maintenance-Classification-API
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

```bash
cp env.example .env
```

Available variables:

| Variable    | Default                                           | Description              |
| ----------- | ------------------------------------------------- | ------------------------ |
| `APP_NAME`  | Machine Predictive Maintenance Classification API | Application display name |
| `VERSION`   | 1.0                                               | API version              |
| `DEBUG`     | false                                             | Debug mode               |
| `HOST`      | 0.0.0.0                                           | Server host              |
| `PORT`      | 8000                                              | Server port              |
| `LOG_LEVEL` | INFO                                              | Logging level            |

---

## ▶️ Usage

### Running locally

```bash
uvicorn main:app --reload
```

Access:

- 🌐 **Web UI**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- 📋 **Prediction Form**: [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)
- 📖 **Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📘 **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running with Docker

```bash
docker-compose build
docker-compose up
```

---

## 📡 API Endpoints

All API endpoints are versioned under `/api/v1/`.

### `GET /api/v1/`

Health check to confirm the API is live.

**Response:**

```json
{
  "message": "Welcome to Machine Predictive Maintenance Classification API",
  "version": "1.0"
}
```

### `POST /api/v1/predict/xgboost`

Accepts machine sensor data, applies feature engineering and preprocessing, and returns:

- `Failure_prediction` — `true` if failure is predicted
- `Failure_probability` — probability score (0.0 – 1.0)

---

## 🌐 Web Pages

| Path              | Description                                               |
| ----------------- | --------------------------------------------------------- |
| `/`               | Landing page with project overview and feature highlights |
| `/predict`        | Interactive form to input sensor data                     |
| `/predict` (POST) | Processes form and displays result with probability gauge |

---

## 📝 Example Request

### Request

```json
POST /api/v1/predict/xgboost
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

### Response

```json
{
  "Failure_prediction": false,
  "Failure_probability": 0.00011
}
```

### Input Schema

| Field                     | Type   | Range         | Description                   |
| ------------------------- | ------ | ------------- | ----------------------------- |
| `Type`                    | string | L, M, H       | Product quality type          |
| `Air temperature [K]`     | float  | 295.3 – 305.4 | Air temperature in Kelvin     |
| `Process temperature [K]` | float  | 305.7 – 313.8 | Process temperature in Kelvin |
| `Rotational speed [rpm]`  | float  | 1168 – 2886   | Rotational speed              |
| `Torque [Nm]`             | float  | 3.8 – 76.6    | Torque                        |
| `Tool wear [min]`         | float  | 0 – 253       | Tool wear time                |

---

## 🧪 Testing

Run the test suite with:

```bash
python -m pytest tests/ -v
```

Tests cover:

- ✅ API health check
- ✅ Prediction with valid input
- ✅ Validation rejection for invalid / missing / out-of-range input
- ✅ Web page rendering (home, form, form submission)

---
