# 🛒 Retail Sales Forecasting & Analysis

An end-to-end machine learning project that predicts weekly retail sales using historical Walmart sales data, and serves predictions through an interactive web dashboard.

## 📌 Problem Statement

Retail businesses need accurate sales forecasts to manage inventory, staffing, and promotions effectively. This project builds a machine learning pipeline to predict weekly sales for a given store and department based on historical trends, store characteristics, and external economic factors.

## 🔍 Key Insights from EDA

- Sales show strong **seasonality**, with major spikes around Thanksgiving and Christmas.
- Holiday weeks have ~7% higher average sales compared to non-holiday weeks.
- **Store type and size** are among the strongest predictors of sales volume — larger, Type A stores consistently outperform others.
- External economic indicators (Temperature, Fuel Price, CPI, Unemployment) have relatively low predictive power compared to store-specific features.

## 🧠 Approach

1. **Data Cleaning & EDA** — Handled missing values, analyzed seasonal trends, and explored relationships between sales and store/department attributes.
2. **Feature Engineering** — Extracted date-based features (Year, Month, Week) and encoded categorical variables.
3. **Modeling** — Compared multiple models:

| Model               | MAE       | RMSE      |
| ------------------- | --------- | --------- |
| Linear Regression   | 14,340    | 21,086    |
| Random Forest       | 2,615     | 5,342     |
| XGBoost (default)   | 2,672     | 4,735     |
| **XGBoost (tuned)** | **2,344** | **4,462** |

4. **Hyperparameter Tuning** — Used RandomizedSearchCV to optimize the XGBoost model, improving MAE by ~12%.
5. **Deployment** — Built an interactive Streamlit dashboard for real-time sales predictions.

## 🚀 Live Demo

🔗 **[Try the live dashboard here](https://retail-sales-forecasting-agvly4nyd2pkkrkcej8zhm.streamlit.app/)**

The dashboard allows users to input store details (Store number, Department, Size, Type, and economic factors) and get an instant weekly sales prediction.

_(Add a screenshot of your dashboard here)_

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **Deployment:** Streamlit
- **Model Persistence:** Joblib

## 📂 Project Structure

## 📊 Dataset

This project uses the [Walmart Sales Forecast dataset](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast) from Kaggle, containing historical weekly sales data across 45 stores and multiple departments, along with store and economic features.

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Waseem-23/retail-sales-forecasting.git
cd retail-sales-forecasting

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

## 📈 Future Improvements

- Incorporate time-series specific models (Prophet, ARIMA) for comparison
- Add SHAP-based explainability for individual predictions
- Deploy the dashboard on Streamlit Cloud / Hugging Face Spaces for public access

## 👤 Author

**Waseem** — BS Computer Science (AI Specialization)
[GitHub](https://github.com/Waseem-23)
