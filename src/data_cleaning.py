import pandas as pd
import numpy as np
import os
import sys

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def load_data(filepath):
    """Load the dataset from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """
    Perform data cleaning on the dataset.
    - Remove unnecessary columns
    - Handle missing values
    - Fix datatype issues
    - Handle duplicate records
    - Validate consistency
    """
    # 1. Remove unnecessary columns
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    # 2. Fix TotalCharges datatype and handle missing values
    # TotalCharges often contains empty strings for customers with 0 tenure
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill missing TotalCharges with 0 (since they have 0 tenure)
    df['TotalCharges'] = df['TotalCharges'].fillna(0)

    # 3. Handle duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    final_rows = len(df)
    if initial_rows > final_rows:
        print(f"Removed {initial_rows - final_rows} duplicate records.")

    # 4. SeniorCitizen mapping (standard convention for this project)
    if df['SeniorCitizen'].dtype != 'object':
        df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

    # 5. Data Consistency Validation
    # Example: Ensure tenure >= 0
    df = df[df['tenure'] >= 0]

    # Ensure MonthlyCharges > 0
    df = df[df['MonthlyCharges'] >= 0]

    return df

def main():
    project_root = get_project_root()
    raw_data_path = os.path.join(project_root, 'data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    processed_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_data.csv')

    try:
        df = load_data(raw_data_path)
        print(f"Loaded raw data with shape: {df.shape}")

        df_cleaned = clean_data(df)
        print(f"Cleaned data shape: {df_cleaned.shape}")

        # Save cleaned data
        os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
        df_cleaned.to_csv(processed_data_path, index=False)
        print(f"Cleaned data saved to {processed_data_path}")

    except Exception as e:
        print(f"Error during data cleaning: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
