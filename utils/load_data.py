import pandas as pd

def load_food_data():

    df = pd.read_csv(
        "data/center_data.csv"
    )

    return df


def load_center_data():

    centers = pd.read_csv(
        "data/food_waste.csv"
    )

    return centers