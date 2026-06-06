# Customer Churn Prediction API Startup Guide

## Installation

1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

## Running the API

1. From the project root, run the following command:
   ```bash
   uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
   ```

## Testing the API

1. Run automated tests:
   ```bash
   pytest backend/tests/test_api.py
   ```

2. Manual test with curl:
   ```bash
   curl -X 'POST' \
     'http://localhost:8000/predict' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
       "gender": "Female",
       "SeniorCitizen": "No",
       "Partner": "Yes",
       "Dependents": "No",
       "tenure": 1,
       "PhoneService": "No",
       "MultipleLines": "No phone service",
       "InternetService": "DSL",
       "OnlineSecurity": "No",
       "OnlineBackup": "Yes",
       "DeviceProtection": "No",
       "TechSupport": "No",
       "StreamingTV": "No",
       "StreamingMovies": "No",
       "Contract": "Month-to-month",
       "PaperlessBilling": "Yes",
       "PaymentMethod": "Electronic check",
       "MonthlyCharges": 29.85,
       "TotalCharges": 29.85
     }'
   ```

## API Documentation

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
