import pandas as pd
import logging
import os
from datetime import datetime

# ---------------------------------------------------
# SETUP LOGGING
# ---------------------------------------------------

os.makedirs("../data/logs", exist_ok=True)

logging.basicConfig(
    filename="../data/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------------------------------------------
# EXTRACT
# ---------------------------------------------------

def extract_data():
    logging.info("Starting data extraction")

    df = pd.read_csv(
        "../data/superstore_clean.csv",
        parse_dates=["order_date", "ship_date"]
    )

    logging.info("Data extracted successfully")
    return df

# ---------------------------------------------------
# TRANSFORM
# ---------------------------------------------------

def transform_data(df):
    logging.info("Starting transformation step")

    df["order_month"] = df["order_date"].dt.to_period("M")

    region_summary = (
        df.groupby("region")
        .agg(total_sales=("sales", "sum"),
             total_profit=("profit", "sum"))
        .reset_index()
    )

    category_summary = (
        df.groupby("category")
        .agg(total_sales=("sales", "sum"),
             total_profit=("profit", "sum"),
             avg_discount=("discount", "mean"))
        .reset_index()
    )

    monthly_summary = (
        df.groupby("order_month")
        .agg(total_sales=("sales", "sum"),
             total_profit=("profit", "sum"))
        .reset_index()
    )

    logging.info("Transformation completed")

    return region_summary, category_summary, monthly_summary

# ---------------------------------------------------
# LOAD
# ---------------------------------------------------

def load_data(region, category, monthly):
    logging.info("Starting load step")

    os.makedirs("../data/aggregates", exist_ok=True)

    region.to_csv("../data/aggregates/sales_by_region.csv", index=False)
    category.to_csv("../data/aggregates/sales_by_category.csv", index=False)
    monthly.to_csv("../data/aggregates/monthly_performance.csv", index=False)

    logging.info("Data saved successfully")

# ---------------------------------------------------
# VALIDATION
# ---------------------------------------------------

def validate_dataset(df, name):
    logging.info(f"Validating {name}")

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    if missing > 0:
        logging.error(f"{name} contains missing values")
        raise ValueError(f"{name} contains missing values")

    if duplicates > 0:
        logging.error(f"{name} contains duplicate rows")
        raise ValueError(f"{name} contains duplicates")

    logging.info(f"{name} passed validation")

# ---------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------

def run_pipeline():
    start_time = datetime.now()
    logging.info("Pipeline started")

    try:
        df = extract_data()

        region, category, monthly = transform_data(df)

        validate_dataset(region, "Region Summary")
        validate_dataset(category, "Category Summary")
        validate_dataset(monthly, "Monthly Summary")

        load_data(region, category, monthly)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

    end_time = datetime.now()
    logging.info(f"Pipeline runtime: {end_time - start_time}")

# ---------------------------------------------------
# RUN SCRIPT
# ---------------------------------------------------

if __name__ == "__main__":
    run_pipeline()