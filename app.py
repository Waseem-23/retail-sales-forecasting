import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Retail Sales Forecaster", layout="centered")

# Load model
model = joblib.load('xgb_sales_model.pkl')

# Title
st.title("🛒 Retail Sales Forecasting")
st.write("Predict weekly sales for a given Store and Department")

# Sidebar Inputs
st.header("Enter Details")

store = st.number_input("Store Number", min_value=1, max_value=45, value=1)
dept = st.number_input("Department Number", min_value=1, max_value=99, value=1)
size = st.number_input("Store Size (sq ft)", min_value=30000, max_value=250000, value=150000)
store_type = st.selectbox("Store Type", options=["A", "B", "C"])
type_map = {"A": 0, "B": 1, "C": 2}

is_holiday = st.checkbox("Is this a Holiday Week?")
temperature = st.slider("Temperature (°F)", min_value=-10, max_value=110, value=60)
fuel_price = st.slider("Fuel Price ($)", min_value=2.0, max_value=5.0, value=3.5)
cpi = st.number_input("CPI (Consumer Price Index)", min_value=100.0, max_value=250.0, value=180.0)
unemployment = st.slider("Unemployment Rate (%)", min_value=3.0, max_value=15.0, value=7.0)

year = st.selectbox("Year", options=[2010, 2011, 2012, 2013])
month = st.selectbox("Month", options=list(range(1, 13)))
week = st.number_input("Week of Year", min_value=1, max_value=52, value=1)

# Predict button
if st.button("Predict Weekly Sales"):
    input_data = pd.DataFrame({
        'Store': [store],
        'Dept': [dept],
        'IsHoliday': [int(is_holiday)],
        'Size': [size],
        'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'Type_encoded': [type_map[store_type]],
        'Year': [year],
        'Month': [month],
        'Week': [week]
    })
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"### Predicted Weekly Sales: ${prediction:,.2f}")