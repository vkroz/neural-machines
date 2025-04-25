import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

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

# Initialize XGBClassifier with modern parameters
model = XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=1,
    gamma=0,
    random_state=42,
    n_estimators=100,
    early_stopping_rounds=10,
    use_label_encoder=False  # Important: prevents deprecation warning
)

# Train the model with validation set
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=10
)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

# Evaluate the model
print("\nModel Evaluation:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature importance
importance = model.feature_importances_
sorted_idx = np.argsort(importance)[::-1]
print("\nFeature Importance:")
for idx in sorted_idx[:5]:  # Top 5 features
    print(f"Feature {idx}: {importance[idx]:.4f}")

# Optional: Grid Search for hyperparameter tuning
param_grid = {
    'max_depth': [3, 6, 9],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

# Uncomment to perform grid search
# grid_search = GridSearchCV(
#     estimator=model,
#     param_grid=param_grid,
#     cv=3,
#     scoring='accuracy',
#     verbose=1
# )
# grid_search.fit(X_train, y_train)
# print("\nBest parameters:", grid_search.best_params_) 