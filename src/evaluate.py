import pandas as pd
import numpy as np
import os
import sys
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix, roc_curve)

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def evaluate_models():
    project_root = get_project_root()
    test_path = os.path.join(project_root, 'data', 'processed', 'test.csv')
    models_dir = os.path.join(project_root, 'models', 'trained_models')
    metrics_dir = os.path.join(project_root, 'models', 'metrics')
    plots_dir = os.path.join(project_root, 'models', 'plots')

    os.makedirs(metrics_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    if not os.path.exists(test_path):
        print("Test data not found.")
        return

    df_test = pd.read_csv(test_path)
    X_test = df_test.drop(columns=['Churn'])
    y_test = df_test['Churn']

    model_files = {
        'Logistic Regression': 'logistic_regression.pkl',
        'Random Forest': 'random_forest.pkl',
        'XGBoost': 'xgboost.pkl'
    }

    results = []
    plt.figure(figsize=(10, 8))

    for name, filename in model_files.items():
        model_path = os.path.join(models_dir, filename)
        if not os.path.exists(model_path):
            print(f"Model {name} not found at {model_path}")
            continue

        model = joblib.load(model_path)
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        # Calculate metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_proba)

        results.append({
            'Model': name,
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'F1': f1,
            'ROC_AUC': auc
        })

        # Plot ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})')

        # Plot Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix - {name}')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        clean_name = name.lower().replace(' ', '_')
        if clean_name == 'random_forest':
            plot_name = 'confusion_matrix_rf.png'
        elif clean_name == 'xgboost':
            plot_name = 'confusion_matrix_xgb.png'
        else:
            plot_name = f'confusion_matrix_{clean_name}.png'

        plt.savefig(os.path.join(plots_dir, plot_name))
        plt.close()

        # Feature Importance for tree-based models
        if hasattr(model, 'feature_importances_'):
            plt.figure(figsize=(10, 12))
            importances = pd.Series(model.feature_importances_, index=X_test.columns)
            importances.nlargest(20).sort_values().plot(kind='barh')
            plt.title(f'Top 20 Feature Importances - {name}')
            if name == 'XGBoost': # Only save one for the chart requested or for the best tree model
                plt.savefig(os.path.join(plots_dir, 'feature_importance.png'))
            plt.close()

    # Save ROC Curve Comparison
    plt.figure(1)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Comparison')
    plt.legend()
    plt.savefig(os.path.join(plots_dir, 'roc_curve.png'))
    plt.close()

    # Save Comparison CSV
    comparison_df = pd.DataFrame(results)
    comparison_df.to_csv(os.path.join(metrics_dir, 'model_comparison.csv'), index=False)
    print("Evaluation completed. Metrics and plots saved.")

if __name__ == "__main__":
    evaluate_models()
