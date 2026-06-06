import pandas as pd
import numpy as np
import os
import sys
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def train_models():
    project_root = get_project_root()
    train_path = os.path.join(project_root, 'data', 'processed', 'train.csv')
    models_dir = os.path.join(project_root, 'models', 'trained_models')
    os.makedirs(models_dir, exist_ok=True)

    if not os.path.exists(train_path):
        print("Train data not found.")
        return

    df_train = pd.read_csv(train_path)
    X_train = df_train.drop(columns=['Churn'])
    y_train = df_train['Churn']

    # 1. Logistic Regression
    print("Training Logistic Regression...")
    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train, y_train)
    joblib.dump(lr, os.path.join(models_dir, 'logistic_regression.pkl'))

    # 2. Random Forest with Hyperparameter Tuning
    print("Tuning Random Forest...")
    rf_param_dist = {
        'n_estimators': randint(50, 200),
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': randint(2, 11)
    }
    rf = RandomForestClassifier(random_state=42)
    rf_search = RandomizedSearchCV(rf, param_distributions=rf_param_dist,
                                   n_iter=10, cv=5, scoring='roc_auc',
                                   random_state=42, n_jobs=-1)
    rf_search.fit(X_train, y_train)
    joblib.dump(rf_search.best_estimator_, os.path.join(models_dir, 'random_forest.pkl'))
    print(f"Best RF params: {rf_search.best_params_}")

    # 3. XGBoost with Hyperparameter Tuning
    print("Tuning XGBoost...")
    xgb_param_dist = {
        'learning_rate': uniform(0.01, 0.3),
        'max_depth': randint(3, 10),
        'n_estimators': randint(50, 200),
        'subsample': uniform(0.6, 0.4)
    }
    xgb = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
    xgb_search = RandomizedSearchCV(xgb, param_distributions=xgb_param_dist,
                                    n_iter=10, cv=5, scoring='roc_auc',
                                    random_state=42, n_jobs=-1)
    xgb_search.fit(X_train, y_train)
    joblib.dump(xgb_search.best_estimator_, os.path.join(models_dir, 'xgboost.pkl'))
    print(f"Best XGB params: {xgb_search.best_params_}")

    print("Model training and tuning completed.")

if __name__ == "__main__":
    train_models()
