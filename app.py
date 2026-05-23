import streamlit as st
import pandas as pd

from utils.load_data import load_food_data, load_center_data

# PAGE CONFIG
st.set_page_config(
    page_title="Food Waste Dashboard",
    layout="wide"
)

# TITLE
st.title("🍽️ Food Waste Analysis Dashboard")

# LOAD DATA
df = load_food_data()
centers = load_center_data()

# SHOW COLUMNS
st.subheader("Dataset Columns")
st.write(df.columns)

# SHOW DATA
st.subheader("Dataset Preview")
st.dataframe(df.head())

# TOTAL RECORDS
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

total_records = df.shape[0]
total_columns = df.shape[1]

col1.metric("Total Records", total_records)
col2.metric("Total Columns", total_columns)
col3.metric("Center Records", centers.shape[0])

# NUMERIC COLUMNS
numeric_cols = df.select_dtypes(include="number").columns

# VISUALIZATION
st.subheader("Visual Analysis")

if len(numeric_cols) > 0:

    selected_col = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    chart_data = (
        df[selected_col]
        .value_counts()
        .reset_index()
    )

    chart_data.columns = ["Value", "Count"]

    st.bar_chart(
        chart_data.set_index("Value")
    )

# CENTER DATA
st.subheader("Fulfilment Center Information")

st.dataframe(centers.head())

# FOOTER
st.markdown("---")
st.markdown("Built using Streamlit and Python")