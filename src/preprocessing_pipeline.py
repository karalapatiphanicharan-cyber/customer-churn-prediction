import pandas as pd
import numpy as np
import os
import sys
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root
from transformers import FeatureEngineer

def build_full_pipeline(numeric_features, categorical_features):
    """
    Build a full preprocessing pipeline including feature engineering.
    """
    # Feature engineering step
    fe_step = ('feature_engineer', FeatureEngineer())

    # Preprocessing step
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Combined pipeline
    full_pipeline = Pipeline(steps=[
        fe_step,
        ('preprocessor', preprocessor)
    ])

    return full_pipeline

def main():
    project_root = get_project_root()
    cleaned_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_data.csv')
    artifacts_dir = os.path.join(project_root, 'artifacts')
    os.makedirs(artifacts_dir, exist_ok=True)

    try:
        if not os.path.exists(cleaned_data_path):
            print("Cleaned data not found. Run data_cleaning.py first.")
            return

        df = pd.read_csv(cleaned_data_path)

        # Define target and features
        target = 'Churn'
        X = df.drop(columns=[target])
        y = df[target]

        # Map target to numeric
        le = LabelEncoder()
        y = le.fit_transform(y)
        joblib.dump(le, os.path.join(artifacts_dir, 'target_encoder.pkl'))

        # Define initial features for the ColumnTransformer (these will be present AFTER FeatureEngineer)
        # We need to know what features the FeatureEngineer produces
        # Base features + New features

        # Original numeric: tenure, MonthlyCharges, TotalCharges
        # New numeric: avg_monthly_spend, total_services, contract_type_risk
        numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_spend', 'total_services', 'contract_type_risk']

        # Original categorical: gender, SeniorCitizen, Partner, Dependents, PhoneService, MultipleLines, InternetService,
        # OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
        # PaperlessBilling, PaymentMethod
        # New categorical: tenure_group, customer_value_segment
        categorical_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                                'tenure_group', 'customer_value_segment']

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Build and fit pipeline
        full_pipeline = build_full_pipeline(numeric_features, categorical_features)

        # Fit on training data
        X_train_processed = full_pipeline.fit_transform(X_train)
        X_test_processed = full_pipeline.transform(X_test)

        # Get feature names after one-hot encoding
        preprocessor = full_pipeline.named_steps['preprocessor']
        cat_encoder = preprocessor.named_transformers_['cat'].named_steps['onehot']
        cat_feature_names = cat_encoder.get_feature_names_out(categorical_features).tolist()
        all_feature_names = numeric_features + cat_feature_names

        # Convert back to DataFrame for saving
        X_train_df = pd.DataFrame(X_train_processed, columns=all_feature_names)
        X_train_df[target] = y_train

        X_test_df = pd.DataFrame(X_test_processed, columns=all_feature_names)
        X_test_df[target] = y_test

        # Save processed datasets
        X_train_df.to_csv(os.path.join(project_root, 'data', 'processed', 'train.csv'), index=False)
        X_test_df.to_csv(os.path.join(project_root, 'data', 'processed', 'test.csv'), index=False)

        # Save artifacts
        joblib.dump(full_pipeline, os.path.join(artifacts_dir, 'preprocessing_pipeline.pkl'))

        # Extract and save individual components for convenience
        joblib.dump(cat_encoder, os.path.join(artifacts_dir, 'encoder.pkl'))
        joblib.dump(preprocessor.named_transformers_['num'].named_steps['scaler'],
                    os.path.join(artifacts_dir, 'scaler.pkl'))

        print("Full preprocessing pipeline completed and artifacts saved.")
        print(f"Train shape: {X_train_df.shape}, Test shape: {X_test_df.shape}")

    except Exception as e:
        print(f"Error during preprocessing pipeline: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
