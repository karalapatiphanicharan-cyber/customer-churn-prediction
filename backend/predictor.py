import pandas as pd
from backend.model_loader import get_model_loader

class ChurnPredictor:
    def __init__(self):
        loader = get_model_loader()
        self.model = loader.model
        self.pipeline = loader.pipeline
        self.target_encoder = loader.target_encoder

    def predict(self, customer_data: dict):
        df = pd.DataFrame([customer_data])

        # Preprocess using the pipeline
        X_processed = self.pipeline.transform(df)

        # Get probability and prediction
        probability = self.model.predict_proba(X_processed)[0, 1]
        prediction_idx = self.model.predict(X_processed)[0]
        prediction = self.target_encoder.inverse_transform([prediction_idx])[0]

        # Determine risk level
        if probability < 0.3:
            risk_level = "Low"
        elif probability < 0.7:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "prediction": "Churn" if prediction == "Yes" else "No Churn",
            "probability": float(probability),
            "risk_level": risk_level
        }
