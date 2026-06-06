import pandas as pd
import numpy as np
import os
import sys

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def create_features(df):
    """
    Create meaningful features for churn prediction.
    - tenure_group
    - avg_monthly_spend
    - total_services
    - contract_type_risk
    - customer_value_segment
    """
    df = df.copy()

    # 1. tenure_group
    bins = [0, 12, 24, 36, 48, 60, 72]
    labels = ['0-12', '12-24', '24-36', '36-48', '48-60', '60-72']
    df['tenure_group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)

    # 2. avg_monthly_spend
    # Use tenure + 1 to avoid division by zero if tenure is 0
    df['avg_monthly_spend'] = df['TotalCharges'] / (df['tenure'].replace(0, 1))

    # 3. total_services
    # Count of active services (excluding PhoneService if it's redundant with MultipleLines)
    # But usually all services: PhoneService, MultipleLines, InternetService, OnlineSecurity,
    # OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
    service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

    # We count only those that are 'Yes'
    df['total_services'] = (df[service_cols] == 'Yes').sum(axis=1)

    # 4. contract_type_risk
    # Month-to-month: High Risk (2), One year: Medium Risk (1), Two year: Low Risk (0)
    contract_risk_map = {'Month-to-month': 2, 'One year': 1, 'Two year': 0}
    df['contract_type_risk'] = df['Contract'].map(contract_risk_map)

    # 5. customer_value_segment
    # Segment based on MonthlyCharges quantiles
    df['customer_value_segment'] = pd.qcut(df['MonthlyCharges'], q=3, labels=['Low', 'Medium', 'High'])

    return df

def main():
    project_root = get_project_root()
    cleaned_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_data.csv')
    feature_data_path = os.path.join(project_root, 'data', 'processed', 'feature_engineered_data.csv')

    try:
        if not os.path.exists(cleaned_data_path):
            print("Cleaned data not found. Run data_cleaning.py first.")
            return

        df = pd.read_csv(cleaned_data_path)
        print(f"Loaded cleaned data with shape: {df.shape}")

        df_featured = create_features(df)
        print(f"Feature engineered data shape: {df_featured.shape}")

        # Save featured data
        df_featured.to_csv(feature_data_path, index=False)
        print(f"Feature engineered data saved to {feature_data_path}")

    except Exception as e:
        print(f"Error during feature engineering: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
