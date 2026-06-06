import pandas as pd
import numpy as np
import os
import sys

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_data(filepath):
    """Load the dataset from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """Perform initial cleaning on the dataset."""
    # Convert TotalCharges to numeric, handling empty strings
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Handle missing values in TotalCharges (usually for new customers with 0 tenure)
    df['TotalCharges'] = df['TotalCharges'].fillna(0)

    # Convert SeniorCitizen to categorical (0/1 to No/Yes) for better visualization
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

    return df

def check_duplicates(df):
    """Check for duplicate records in the dataset."""
    duplicates = df.duplicated().sum()
    return duplicates

def get_summary_stats(df):
    """Return summary statistics of the dataset."""
    return df.describe(include='all')

if __name__ == "__main__":
    from utils import get_project_root

    # Use robust path detection
    project_root = get_project_root()
    data_path = os.path.join(project_root, 'data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')

    try:
        df = load_data(data_path)
        print(f"Duplicates found: {check_duplicates(df)}")
        df = clean_data(df)
        print("Data loaded and cleaned successfully.")
        print(f"Shape: {df.shape}")
        # print(df.info())
    except Exception as e:
        print(f"Error: {e}")
