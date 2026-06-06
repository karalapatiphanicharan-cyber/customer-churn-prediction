import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add src to path to import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_preprocessing import load_data, clean_data, check_duplicates
from utils import save_plot, ensure_dir, get_project_root

def perform_eda(df, output_dir='reports/figures/'):
    """Perform exploratory data analysis and save visualizations."""
    ensure_dir(output_dir)

    # Set the style for seaborn
    sns.set_theme(style="whitegrid")

    # Check duplicates and missing values (printing for info during run)
    print(f"Duplicates: {check_duplicates(df)}")
    print(f"Missing values:\n{df.isnull().sum()}")

    # 1. Target variable distribution (Churn)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Churn', data=df, hue='Churn', palette='viridis', legend=False)
    plt.title('Distribution of Churn')
    save_plot('churn_distribution.png', output_dir)

    # 2. Numerical feature distributions
    num_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    plt.figure(figsize=(15, 5))
    for i, feature in enumerate(num_features):
        plt.subplot(1, 3, i+1)
        sns.histplot(df[feature], kde=True, color='skyblue')
        plt.title(f'Distribution of {feature}')
    save_plot('numerical_distributions.png', output_dir)

    # 3. Categorical feature distributions (Selection of key ones)
    cat_features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'InternetService', 'Contract']
    plt.figure(figsize=(20, 15))
    for i, feature in enumerate(cat_features):
        plt.subplot(3, 2, i+1)
        sns.countplot(x=feature, data=df, hue='Churn', palette='magma')
        plt.title(f'Churn by {feature}')
    save_plot('categorical_distributions.png', output_dir)

    # 4. Correlation heatmap
    plt.figure(figsize=(10, 8))
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    save_plot('correlation_heatmap.png', output_dir)

    # 5. Customer tenure analysis
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[df['Churn'] == 'Yes']['tenure'], label='Churn: Yes', fill=True)
    sns.kdeplot(df[df['Churn'] == 'No']['tenure'], label='Churn: No', fill=True)
    plt.title('Tenure Distribution by Churn')
    plt.legend()
    save_plot('tenure_by_churn.png', output_dir)

    # 6. Monthly charges analysis
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df[df['Churn'] == 'Yes']['MonthlyCharges'], label='Churn: Yes', fill=True)
    sns.kdeplot(df[df['Churn'] == 'No']['MonthlyCharges'], label='Churn: No', fill=True)
    plt.title('Monthly Charges Distribution by Churn')
    plt.legend()
    save_plot('monthly_charges_by_churn.png', output_dir)

    # 7. Total charges analysis
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Churn', y='TotalCharges', data=df, hue='Churn', palette='Set2', legend=False)
    plt.title('Total Charges by Churn')
    save_plot('total_charges_boxplot.png', output_dir)

    # 8. Payment Method vs Churn
    plt.figure(figsize=(12, 6))
    sns.countplot(x='PaymentMethod', hue='Churn', data=df, palette='Set1')
    plt.title('Churn by Payment Method')
    plt.xticks(rotation=45)
    save_plot('payment_method_by_churn.png', output_dir)

def main():
    # Use robust path detection
    project_root = get_project_root()
    data_path = os.path.join(project_root, 'data', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')
    output_dir = os.path.join(project_root, 'reports', 'figures')

    # Load and clean data
    print("Loading and cleaning data...")
    df = load_data(data_path)
    df = clean_data(df)

    # Perform EDA
    print("Performing EDA and generating visualizations...")
    perform_eda(df, output_dir)
    print("EDA completed successfully.")

if __name__ == "__main__":
    main()
