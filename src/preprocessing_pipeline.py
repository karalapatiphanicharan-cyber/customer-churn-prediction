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

def build_pipeline(numeric_features, categorical_features):
    """
    Build a preprocessing pipeline with scaling and encoding.
    """
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

    return preprocessor

def main():
    project_root = get_project_root()
    feature_data_path = os.path.join(project_root, 'data', 'processed', 'feature_engineered_data.csv')
    artifacts_dir = os.path.join(project_root, 'artifacts')
    os.makedirs(artifacts_dir, exist_ok=True)

    try:
        if not os.path.exists(feature_data_path):
            print("Feature engineered data not found. Run feature_engineering.py first.")
            return

        df = pd.read_csv(feature_data_path)

        # Define target and features
        target = 'Churn'
        X = df.drop(columns=[target])
        y = df[target]

        # Map target to numeric
        le = LabelEncoder()
        y = le.fit_transform(y)
        joblib.dump(le, os.path.join(artifacts_dir, 'target_encoder.pkl'))

        # Identify numeric and categorical columns
        # Note: tenure_group and customer_value_segment are categorical
        categorical_features = X.select_dtypes(include=['object', 'category']).columns.tolist()
        numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

        print(f"Numeric features: {numeric_features}")
        print(f"Categorical features: {categorical_features}")

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Build and fit pipeline
        preprocessor = build_pipeline(numeric_features, categorical_features)

        # Fit on training data
        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)

        # Get feature names after one-hot encoding
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
        joblib.dump(preprocessor, os.path.join(artifacts_dir, 'preprocessing_pipeline.pkl'))

        # Extract and save individual components for convenience (as requested)
        joblib.dump(preprocessor.named_transformers_['cat'].named_steps['onehot'],
                    os.path.join(artifacts_dir, 'encoder.pkl'))
        joblib.dump(preprocessor.named_transformers_['num'].named_steps['scaler'],
                    os.path.join(artifacts_dir, 'scaler.pkl'))

        print("Preprocessing pipeline completed and artifacts saved.")
        print(f"Train shape: {X_train_df.shape}, Test shape: {X_test_df.shape}")

    except Exception as e:
        print(f"Error during preprocessing pipeline: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
