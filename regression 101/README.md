# Home Price Prediction using Linear Regression

This project demonstrates a complete end-to-end machine learning lifecycle for a simple linear regression model to predict house prices.

## Overview

The implementation showcases the following steps in the ML lifecycle:

1. **Data Loading**: Loading the California housing dataset from scikit-learn
2. **Exploratory Data Analysis**: Analyzing the dataset structure and relationships
3. **Feature Selection**: Selecting the most relevant features based on correlation
4. **Data Preprocessing**: Splitting the data and standardizing the features
5. **Model Training**: Training a linear regression model using scikit-learn
6. **Model Evaluation**: Evaluating the model using various metrics (RMSE, MAE, R²)
7. **Model Inference**: Using the trained model to make predictions on new data

## Files

- `home_price_regression.py`: The main Python script implementing the end-to-end ML pipeline
- `california_housing_regression.ipynb`: Jupyter notebook version of the implementation (if you prefer interactive exploration)

## Requirements

The following Python packages are required:

```
scikit-learn
pandas
numpy
matplotlib
seaborn
```

You can install them using pip:

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

## Usage

To run the script:

```bash
python home_price_regression.py
```

This will:
1. Load the California housing dataset from scikit-learn
2. Perform exploratory data analysis and save visualization plots
3. Train a linear regression model
4. Evaluate the model and display performance metrics
5. Demonstrate inference with sample house data

## Dataset

The script uses the California housing dataset from scikit-learn, which contains information about housing in California districts. The target variable is the median house value for California districts, expressed in hundreds of thousands of dollars.

## Output

The script generates several visualization files:
- `price_distribution.png`: Distribution of house prices in the dataset
- `feature_correlations.png`: Scatter plots showing correlations between top features and house prices
- `actual_vs_predicted.png`: Comparison of actual vs. predicted house prices
- `residuals.png`: Residual plot for model evaluation

## Model Details

The implementation uses a simple linear regression model with the following components:
- Feature standardization using `StandardScaler`
- Linear regression from scikit-learn
- The top 5 features most correlated with the target variable are selected for simplicity

## Extensions

For a real-world application, you might want to consider:
- More sophisticated feature engineering
- Handling categorical variables
- Addressing outliers and missing values more thoroughly
- Trying more complex models
- Implementing cross-validation
- Model deployment strategies 