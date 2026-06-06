import pandas as pd
import joblib
import os
import sys

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

class ChurnPredictor:
    def __init__(self, artifacts_dir=None):
        if artifacts_dir is None:
            project_root = get_project_root()
            artifacts_dir = os.path.join(project_root, 'artifacts')

        self.pipeline = joblib.load(os.path.join(artifacts_dir, 'preprocessing_pipeline.pkl'))
        self.model = joblib.load(os.path.join(artifacts_dir, 'best_model.pkl'))
        self.target_encoder = joblib.load(os.path.join(artifacts_dir, 'target_encoder.pkl'))

    def predict(self, df):
        """
        Predict churn for a given DataFrame of raw features.
        Note: Assumes data has been cleaned and feature engineered if using raw input.
        If using the saved pipeline, it should handle the encoding/scaling.
        """
        # Preprocessing (This depends on how the pipeline was saved)
        # If the pipeline includes the full ColumnTransformer, we use it.
        X_processed = self.pipeline.transform(df)

        # Prediction
        preds = self.model.predict(X_processed)

        # Inverse transform target if needed
        return self.target_encoder.inverse_transform(preds)

    def predict_proba(self, df):
        """
        Predict churn probability.
        """
        X_processed = self.pipeline.transform(df)
        return self.model.predict_proba(X_processed)[:, 1]

def get_predictor():
    return ChurnPredictor()

if __name__ == "__main__":
    # Example usage with a sample from test data (using pre-feature engineered data for simplicity in test)
    project_root = get_project_root()
    test_path = os.path.join(project_root, 'data', 'processed', 'feature_engineered_data.csv')
    if os.path.exists(test_path):
        df = pd.read_csv(test_path).head(5)
        X = df.drop(columns=['Churn'])

        predictor = get_predictor()
        predictions = predictor.predict(X)
        probabilities = predictor.predict_proba(X)

        print("Sample Predictions:", predictions)
        print("Sample Probabilities:", probabilities)
