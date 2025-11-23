import pandas as pd

def transform_data():
    """Returns the already cleaned dataset"""
    df = pd.read_csv("data/clean_sales.csv")
    return df


if __name__ == "__main__":
    df = transform_data()
    print(df.head())
    print("\n✅ transform_data() ran successfully")

