import pandas as pd
import numpy as np
import os
import sys
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Ensure project root is in path to allow src package imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_project_root
from src.transformers import FeatureEngineer

def build_full_pipeline(numeric_features, categorical_features):
    fe_step = ('feature_engineer', FeatureEngineer())

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
        target = 'Churn'
        X = df.drop(columns=[target])
        y = df[target]

        le = LabelEncoder()
        y = le.fit_transform(y)
        joblib.dump(le, os.path.join(artifacts_dir, 'target_encoder.pkl'))

        numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_spend', 'total_services', 'contract_type_risk']
        categorical_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                                'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
                                'tenure_group', 'customer_value_segment']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        full_pipeline = build_full_pipeline(numeric_features, categorical_features)
        X_train_processed = full_pipeline.fit_transform(X_train)
        X_test_processed = full_pipeline.transform(X_test)

        preprocessor = full_pipeline.named_steps['preprocessor']
        cat_encoder = preprocessor.named_transformers_['cat'].named_steps['onehot']
        cat_feature_names = cat_encoder.get_feature_names_out(categorical_features).tolist()
        all_feature_names = numeric_features + cat_feature_names

        X_train_df = pd.DataFrame(X_train_processed, columns=all_feature_names)
        X_train_df[target] = y_train
        X_test_df = pd.DataFrame(X_test_processed, columns=all_feature_names)
        X_test_df[target] = y_test

        X_train_df.to_csv(os.path.join(project_root, 'data', 'processed', 'train.csv'), index=False)
        X_test_df.to_csv(os.path.join(project_root, 'data', 'processed', 'test.csv'), index=False)

        joblib.dump(full_pipeline, os.path.join(artifacts_dir, 'preprocessing_pipeline.pkl'))
        joblib.dump(cat_encoder, os.path.join(artifacts_dir, 'encoder.pkl'))
        joblib.dump(preprocessor.named_transformers_['num'].named_steps['scaler'],
                    os.path.join(artifacts_dir, 'scaler.pkl'))

        print("Full preprocessing pipeline completed and artifacts saved.")

    except Exception as e:
        print(f"Error during preprocessing pipeline: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
