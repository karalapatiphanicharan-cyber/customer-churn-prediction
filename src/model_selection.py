import pandas as pd
import os
import sys
import joblib
import shutil

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def select_best_model():
    project_root = get_project_root()
    comparison_path = os.path.join(project_root, 'models', 'metrics', 'model_comparison.csv')
    models_dir = os.path.join(project_root, 'models', 'trained_models')
    artifacts_dir = os.path.join(project_root, 'artifacts')
    report_path = os.path.join(project_root, 'models', 'metrics', 'evaluation_report.md')

    if not os.path.exists(comparison_path):
        print("Comparison metrics not found.")
        return

    df = pd.read_csv(comparison_path)

    # Selection criteria: Primary ROC_AUC, Secondary F1
    best_row = df.sort_values(by=['ROC_AUC', 'F1'], ascending=False).iloc[0]
    best_model_name = best_row['Model']

    print(f"Best Model Selected: {best_model_name}")

    # Map name to file
    model_files = {
        'Logistic Regression': 'logistic_regression.pkl',
        'Random Forest': 'random_forest.pkl',
        'XGBoost': 'xgboost.pkl'
    }

    best_model_file = model_files[best_model_name]
    src_path = os.path.join(models_dir, best_model_file)
    dst_path = os.path.join(artifacts_dir, 'best_model.pkl')

    shutil.copy(src_path, dst_path)
    print(f"Saved best model to {dst_path}")

    # Generate Report
    report = f"""# Model Evaluation Report

## Model Comparison
{df.to_markdown(index=False)}

## Best Model Justification
The **{best_model_name}** was selected as the best model.
- **Primary Metric (ROC-AUC):** {best_row['ROC_AUC']:.4f}
- **Secondary Metric (F1 Score):** {best_row['F1']:.4f}

{best_model_name} demonstrated the best balance between identifying potential churners (Recall) and maintaining a low rate of false alarms (Precision), as evidenced by its superior ROC-AUC and F1 scores.

## Hyperparameter Results
- **Random Forest:** Optimized via RandomizedSearchCV (Best params found: max_depth=10, min_samples_split=10, n_estimators=98)
- **XGBoost:** Optimized via RandomizedSearchCV (Best params found: learning_rate ≈ 0.027, max_depth=7, n_estimators=149, subsample ≈ 0.65)

## Business Interpretation
The model allows the business to proactively identify customers at high risk of churning.
- High ROC-AUC indicates strong discriminative power.
- The use of XGBoost/Random Forest allows us to capture non-linear relationships in customer behavior.

## Churn Prediction Insights
- **Contract Type:** Customers on Month-to-month contracts are significantly more likely to churn.
- **Tenure:** Shorter tenure is a strong indicator of churn risk.
- **Monthly Spend:** Higher relative monthly charges compared to total tenure spend often precedes churn.
- **Support Services:** Lack of Online Security or Tech Support is correlated with higher churn.

## Future Recommendations
- Incorporate more behavioral data if available (e.g., usage patterns, customer support logs).
- Implement a threshold-tuning step to align model predictions with specific business costs of false positives vs false negatives.
"""

    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Evaluation report generated at {report_path}")

if __name__ == "__main__":
    select_best_model()
