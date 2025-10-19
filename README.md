# House Price Prediction using Machine Learning

An end-to-end **Machine Learning Regression Project** that predicts house prices based on features like **location**, **area (sq. ft)**, **bedrooms**, and **bathrooms**.  
The project focuses heavily on **real-world data cleaning**, **feature engineering**, and **outlier detection** using logical, business-driven assumptions.

---

## Project Highlights

 **Advanced Data Cleaning**
  - Removed inconsistent records where 3BHK homes were cheaper than 2BHK in the same area.
  - Fixed extreme **price-per-square-foot** anomalies (₹267 to ₹12,000,000) using standard deviation thresholds.
  - Removed homes with **bathrooms > (bedrooms + 2)** — considered unrealistic outliers.
  - Applied minimum **300 sq. ft per bedroom rule** (e.g., 2BHK ≥ 600 sq. ft).

- **Feature Engineering**
  - Created `price_per_sqft` feature for better normalization.
  - One-hot encoded **location column** to handle categorical data.
  - Grouped all locations with fewer than 10 listings into an **"Other"** category (dimensionality reduction).
  - Normalized numerical features for stable regression performance.

-  **Model Building & Comparison**
  - Compared **Linear Regression**, **Lasso Regression**, and **Decision Tree Regressor**.
  - Used **K-Fold Cross Validation (Greekssaeve CV)** for unbiased model evaluation.
  - **Linear Regression** achieved the best and most stable performance.

   **Evaluation Metrics**
  - Measured **Accuracy**, 
  - Visualized model results using **Matplotlib**.

-  **Flask Deployment**
  - Built a Flask web app allowing users to input location, area, bedrooms, and bathrooms.
  - Frontend dynamically extracts location and passes it to the backend model.
  - Predicts and displays estimated house price instantly.
  


---

## Tech Stack

| Category | Tools Used |
|-----------|-------------|
| Programming | Python |
| Libraries | Pandas, NumPy, Scikit-learn, Matplotlib |
| Backend | Flask |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |


