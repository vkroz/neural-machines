#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Home Price Prediction using Linear Regression
=============================================

This script demonstrates a complete machine learning lifecycle for a simple linear regression model:
1. Loading data from scikit-learn
2. Exploratory data analysis
3. Data preprocessing
4. Model training
5. Model evaluation
6. Model inference
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.pipeline import Pipeline

# Set plotting style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

def load_data():
    """Load the California housing dataset from scikit-learn"""
    print("Loading California housing dataset from scikit-learn...")
    
    # Load the dataset
    housing = fetch_california_housing()
    
    # Create a pandas DataFrame
    df = pd.DataFrame(housing.data, columns=housing.feature_names)
    df['MedHouseValue'] = housing.target  # Target variable
    
    print(f"Dataset shape: {df.shape}")
    print(df.head())
    
    # Print feature descriptions
    print("\nFeature descriptions:")
    for l in housing.DESCR.splitlines():
        print(l)
    
    return df

def explore_data(df):
    """Perform exploratory data analysis"""
    print("\n--- Exploratory Data Analysis ---")
    
    # Check for missing values
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values[missing_values > 0])
    
    # Basic statistics of numerical features
    print("\nBasic statistics:")
    print(df.describe())
    
    # Distribution of the target variable (MedHouseValue)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['MedHouseValue'], kde=True)
    plt.title('Distribution of House Prices')
    plt.xlabel('Median House Value (100k$)')
    plt.ylabel('Frequency')
    plt.savefig('price_distribution.png')
    plt.close()
    print("Saved price distribution plot to 'price_distribution.png'")
    
    # Correlation between numerical features and the target
    correlation = df.corr()['MedHouseValue'].sort_values(ascending=False)
    print("\nFeatures correlated with MedHouseValue:")
    print(correlation)  # Including MedHouseValue itself
    
    # Visualize the top 5 correlated features with MedHouseValue
    top_features = correlation[1:6].index  # Exclude MedHouseValue itself
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    for i, feature in enumerate(top_features):
        sns.scatterplot(x=feature, y='MedHouseValue', data=df, ax=axes[i])
        axes[i].set_title(f'{feature} vs MedHouseValue')
    
    plt.tight_layout()
    plt.savefig('feature_correlations.png')
    plt.close()
    print("Saved feature correlation plots to 'feature_correlations.png'")
    
    return correlation

def preprocess_data(df, correlation):
    """Preprocess the data for model training"""
    print("\n--- Data Preprocessing ---")
    
    # Select features based on correlation analysis
    # We'll use the top correlated numerical features for simplicity
    selected_features = correlation[1:6].index.tolist()
    print(f"Selected features: {selected_features}")
    
    # Prepare the data
    X = df[selected_features]
    y = df['MedHouseValue']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    return X_train, X_test, y_train, y_test, selected_features

def train_model(X_train, y_train, selected_features):
    """Train the linear regression model"""
    print("\n--- Model Training ---")
    
    # Create a pipeline with preprocessing and model
    pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Standardize features
        ('regressor', LinearRegression())  # Linear regression model
    ])
    
    # Train the model
    pipeline.fit(X_train, y_train)
    
    # Get the coefficients
    coefficients = pipeline.named_steps['regressor'].coef_
    intercept = pipeline.named_steps['regressor'].intercept_
    
    # Display the model coefficients
    coef_df = pd.DataFrame({'Feature': selected_features, 'Coefficient': coefficients})
    print("Model Coefficients:")
    print(coef_df)
    print(f"Intercept: {intercept:.2f}")
    
    return pipeline

def evaluate_model(pipeline, X_test, y_test):
    """Evaluate the trained model"""
    print("\n--- Model Evaluation ---")
    
    # Make predictions on the test set
    y_pred = pipeline.predict(X_test)
    
    # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Display the metrics
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    # Visualize actual vs predicted values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted House Prices')
    plt.savefig('actual_vs_predicted.png')
    plt.close()
    print("Saved actual vs predicted plot to 'actual_vs_predicted.png'")
    
    # Plot residuals
    residuals = y_test - y_pred
    
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Predicted Prices')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.savefig('residuals.png')
    plt.close()
    print("Saved residuals plot to 'residuals.png'")
    
    return y_pred

def model_inference(pipeline, df, selected_features):
    """Use the trained model for inference on new data"""
    print("\n--- Model Inference ---")
    
    # Create a function for making predictions
    def predict_house_price(features_dict):
        # Convert input dictionary to DataFrame
        input_df = pd.DataFrame([features_dict])
        
        # Ensure all required features are present
        for feature in selected_features:
            if feature not in input_df.columns:
                raise ValueError(f"Missing required feature: {feature}")
        
        # Make prediction
        predicted_price = pipeline.predict(input_df[selected_features])[0]
        return predicted_price
    
    # Example: Predict prices for sample houses
    # We'll use the median values from our dataset as a starting point
    sample_house = {}
    for feature in selected_features:
        sample_house[feature] = df[feature].median()
    
    print("Sample house features:")
    for feature, value in sample_house.items():
        print(f"{feature}: {value}")
    
    predicted_price = predict_house_price(sample_house)
    print(f"\nPredicted house price: ${predicted_price:.2f} (in 100k$)")
    
    # Create a more expensive house by increasing the values by 20%
    expensive_house = {}
    for feature in selected_features:
        expensive_house[feature] = df[feature].median() * 1.2
    
    print("\nExpensive house features:")
    for feature, value in expensive_house.items():
        print(f"{feature}: {value}")
    
    predicted_price = predict_house_price(expensive_house)
    print(f"\nPredicted house price: ${predicted_price:.2f} (in 100k$)")
    
    # Create a less expensive house by decreasing the values by 20%
    cheaper_house = {}
    for feature in selected_features:
        cheaper_house[feature] = df[feature].median() * 0.8
    
    print("\nCheaper house features:")
    for feature, value in cheaper_house.items():
        print(f"{feature}: {value}")
    
    predicted_price = predict_house_price(cheaper_house)
    print(f"\nPredicted house price: ${predicted_price:.2f} (in 100k$)")

def main():
    """Main function to run the end-to-end ML pipeline"""
    print("=== Home Price Prediction using Linear Regression ===")
    
    # Step 1: Load data
    df = load_data()
    
    # Step 2: Explore data
    correlation = explore_data(df)
    
    # Step 3: Preprocess data
    X_train, X_test, y_train, y_test, selected_features = preprocess_data(df, correlation)
    
    # Step 4: Train model
    pipeline = train_model(X_train, y_train, selected_features)
    
    # Step 5: Evaluate model
    y_pred = evaluate_model(pipeline, X_test, y_test)
    
    # Step 6: Model inference
    model_inference(pipeline, df, selected_features)
    
    print("\n=== ML Pipeline Complete ===")
    print("This example demonstrated the complete machine learning lifecycle:")
    print("1. Data Loading: Loaded the California housing dataset from scikit-learn")
    print("2. Exploratory Data Analysis: Analyzed the dataset structure and relationships")
    print("3. Feature Selection: Selected the most relevant features based on correlation")
    print("4. Data Preprocessing: Split the data and standardized the features")
    print("5. Model Training: Trained a linear regression model using scikit-learn")
    print("6. Model Evaluation: Evaluated the model using various metrics (RMSE, MAE, R²)")
    print("7. Model Inference: Used the trained model to make predictions on new data")

if __name__ == "__main__":
    main() 