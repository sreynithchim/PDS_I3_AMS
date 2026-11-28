from pathlib import Path

import pandas as pd

def load_sales(path):
    df = pd.read_csv(path)
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df

def total_by_product(df):
    totals = df.groupby("product")["revenue"].sum()
    return totals.sort_values(ascending=False)


def best_seller(df):
    return total_by_product(df).idxmax()

if __name__ == "__main__":
    demo = load_sales(Path(__file__).parent / "sales.csv")
    print("Self-test, best seller:", best_seller(demo))