import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import xgboost as xgb

# Generate synthetic data
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create DMatrix for XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Define parameters
params = {
    'objective': 'binary:logistic',  # for binary classification
    'eval_metric': 'logloss',        # evaluation metric
    'max_depth': 6,                  # maximum depth of trees
    'learning_rate': 0.1,           # learning rate
    'subsample': 0.8,               # subsample ratio of training instances
    'colsample_bytree': 0.8,        # subsample ratio of columns when constructing each tree
    'min_child_weight': 1,          # minimum sum of instance weight needed in a child
    'gamma': 0,                     # minimum loss reduction required to make a further partition
    'random_state': 42
}

# Train the model
num_rounds = 100
evallist = [(dtrain, 'train'), (dtest, 'eval')]
model = xgb.train(
    params,
    dtrain,
    num_rounds,
    evallist,
    early_stopping_rounds=10,
    verbose_eval=10
)

# Make predictions
y_pred = model.predict(dtest)
y_pred_binary = [1 if x > 0.5 else 0 for x in y_pred]

# Evaluate the model
print("\nModel Evaluation:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_binary):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_binary))

# Feature importance
importance = model.get_score(importance_type='weight')
importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)
print("\nFeature Importance:")
for feature, score in importance[:5]:  # Top 5 features
    print(f"Feature {feature}: {score}") 