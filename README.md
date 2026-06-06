# Customer Churn Prediction Platform

A full-stack Machine Learning application that predicts customer churn for a telecommunications company using an XGBoost model, FastAPI backend, and React dashboard.

## Live Demo

### Frontend
https://customer-churn-prediction-neon.vercel.app

### Backend API
https://customer-churn-prediction-q60l.onrender.com

### API Documentation
https://customer-churn-prediction-q60l.onrender.com/docs

---

## Project Overview

Customer churn is one of the most important business challenges in the telecom industry. This project predicts whether a customer is likely to leave the service based on demographic information, subscription details, billing behavior, and service usage patterns.

The system provides:

- Real-time churn prediction
- Churn probability score
- Risk categorization
- Feature importance visualization
- Interactive analytics dashboard

---

## Features

### Machine Learning

- Customer churn prediction using XGBoost
- Feature engineering pipeline
- Model evaluation and selection
- Probability-based predictions
- Serialized production-ready model

### Explainable AI

- SHAP-based feature analysis
- Global feature importance visualization
- Customer risk insights

### Backend

- FastAPI REST API
- Input validation using Pydantic
- Health monitoring endpoint
- Production-ready architecture

### Frontend

- React + Vite
- Tailwind CSS
- Responsive design
- Interactive dashboard
- Risk gauge visualization
- Real-time API integration

---

## Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Recharts

### Deployment

- Render (Backend)
- Vercel (Frontend)
- GitHub

---

## Project Structure

```text
customer-churn-prediction/
│
├── backend/
│   ├── routes/
│   ├── tests/
│   ├── app.py
│   ├── predictor.py
│   ├── model_loader.py
│   └── schemas.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   └── package.json
│
├── data/
├── models/
├── reports/
├── artifacts/
└── README.md
```

---

## Machine Learning Workflow

```text
Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Model Training
    ↓
XGBoost Model
    ↓
Model Evaluation
    ↓
SHAP Analysis
    ↓
FastAPI Deployment
    ↓
React Dashboard
```

---

## API Endpoints

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Customer Churn Prediction API"
}
```

---

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Predict Customer Churn

```http
POST /predict
```

Returns:

```json
{
  "prediction": "Churn",
  "probability": 0.79,
  "risk_level": "High"
}
```

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/karalapatiphanicharan-cyber/customer-churn-prediction.git
cd customer-churn-prediction
```

---

### Backend Setup

```bash
pip install -r backend/requirements.txt
```

Run backend:

```bash
uvicorn backend.app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd frontend
npm install
```

Create:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Run:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Model Information

### Algorithm

XGBoost Classifier

### Prediction Target

Customer Churn

### Input Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Tech Support
- Device Protection
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Monthly Charges
- Total Charges

---

## Dashboard Features

### Customer Input Form

Collects customer information for prediction.

### Prediction Card

Displays:

- Churn / No Churn
- Churn Probability
- Risk Category

### Risk Gauge

Visual risk indicator.

### Feature Importance

Displays top churn drivers.

---

## Deployment

### Frontend

Hosted on Vercel:

https://customer-churn-prediction-neon.vercel.app

### Backend

Hosted on Render:

https://customer-churn-prediction-q60l.onrender.com

---

## Future Improvements

- User authentication
- Batch prediction uploads
- Individual SHAP explanations
- Advanced analytics dashboard
- Model retraining pipeline
- Docker containerization
- CI/CD automation

---

## Screenshots

### Dashboard

Add screenshot here.

### Prediction Results

Add screenshot here.

### Feature Importance

Add screenshot here.

---

## Author

**Phani Charan**

GitHub:

https://github.com/karalapatiphanicharan-cyber

---

## License

This project is developed for educational, research, and portfolio purposes.
