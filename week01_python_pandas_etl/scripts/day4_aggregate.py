import pandas as pd
import os

os.makedirs("../data/aggregates", exist_ok=True)

df = pd.read_csv(
    "../data/superstore_clean.csv",
    parse_dates=["order_date", "ship_date"]
)

region_summary = (
    df.groupby("region")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        avg_profit=("profit", "mean")
    )
    .reset_index()
)

region_summary.to_csv(
    "../data/aggregates/sales_by_region.csv",
    index=False
)

category_summary = (
    df.groupby("category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit","sum"),
        avg_discount=("discount", "mean")
    )
    .reset_index()
)

category_summary.to_csv(
    "../data/aggregates/sales_by_category.csv",
    index=False
)

df["order_month"] = df["order_date"].dt.to_period("M")

monthly_summary = (
    df.groupby("order_month")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
    .reset_index()
)

monthly_summary.to_csv(
    "../data/aggregates/monthly_performance.csv",
    index=False
)

print("\nMonthly summary dtypes:")
print(monthly_summary.dtypes)
