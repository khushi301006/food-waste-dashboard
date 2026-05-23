import plotly.express as px

def waste_by_category(df):

    chart = px.bar(
        df,
        x="category",
        y="food_waste_kg",
        color="category",
        title="Food Waste by Category"
    )

    return chart


def waste_by_city(df):

    chart = px.pie(
        df,
        names="city",
        values="food_waste_kg",
        title="Waste Distribution by City"
    )

    return chart


def monthly_trend(df):

    chart = px.line(
        df,
        x="date",
        y="food_waste_kg",
        title="Monthly Food Waste Trend"
    )

    return chart