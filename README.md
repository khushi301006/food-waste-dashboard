# Food Waste Reduction Analytics Dashboard

## Overview
The Food Waste Reduction Analytics project analyzes restaurant food waste data to identify waste patterns, predict food demand, and optimize inventory management. An interactive dashboard is developed using Python and Streamlit to visualize food wastage trends, seasonal demand, and operational insights, helping restaurants reduce food waste and improve efficiency

## Problem Statement
Restaurants waste large amounts of food daily due to overproduction, poor demand forecasting, seasonal changes, and inefficient inventory management. This project aims to analyze food waste patterns and build a Food Waste Prediction Dashboard to help restaurants reduce wastage, optimize inventory, improve demand prediction, and increase operational efficiency.

## Features
- KPI Dashboard
- Waste Analysis
- Demand Prediction
- Inventory Optimization
- Interactive Visualizations

## Dataset Used
food_wastage_data from kaggle

- Type of Food
- Number of Guests
- Event Type
- Quantity of Food
- Storage Conditions
- Purchase History
- Seasonality
- Preparation Method
- Geographical Location
- Pricing
- Wastage Food Amount

fulfilment_center_info from kaggle

- center_id
- city_code
- region_code
- center_type
- op_area


## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly

## Project Structure
```plaintext
food_waste_dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── food_waste.csv
│   └── center_data.csv
│
├── utils/
│   ├── __init__.py
│   ├── load_data.py
│   └── charts.py
```

## Run Project

```bash
streamlit run app.py
