# 🏠 House Price Prediction Web App

A machine learning-powered web application built with **Flask**, designed to predict housing prices in **Bangalore, India**. Users can input square footage, number of BHKs, bathrooms, and select a location to get an estimated property price.

This project uses real-world housing data and compares multiple regression models to select the most accurate one for deployment.

---

## 🔍 Project Overview

- Data cleaning and preprocessing
- Feature engineering with one-hot encoding for location
- Training and evaluating multiple ML models
- Saving the best model using `pickle`
- Building a Flask server to expose a web interface
- Integrating a frontend form and backend prediction pipeline

---

## 📊 Model Comparison

| Model              | Best Score (R²)  | Best Parameters                               |
|--------------------|------------------|----------------------------------------------|
| Linear Regression  | **0.859956**     | `{'fit_intercept': False}`                   |
| Lasso Regression   | 0.701111         | `{'alpha': 1, 'selection': 'random'}`        |
| Decision Tree      | 0.769444         | `{'criterion': 'friedman_mse', 'splitter': 'best'}`|

> 🏆 **Linear Regression** achieved the highest R² score and was selected for deployment.

---

## 🧠 Final Model Details

- 📦 **Model File**: `home_prices_model.pickle`
- 📁 **Features Used**: `total_sqft`, `bath`, `bhk`, and one-hot encoded `location`
- 📌 **Training Method**: GridSearchCV for hyperparameter tuning
- 📊 **Target**: Price in Lakhs

---
