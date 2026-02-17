import pandas as pd
import os
import logging

# Ensure directories exist
os.makedirs("../data/logs", exist_ok=True)
os.makedirs("../data/validation", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="../data/logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

validation_results = []

def validate_dataset(df, name):
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    logging.info(f"Validating {name}")

    result = {
        "dataset": name,
        "missing_values": missing,
        "duplicate_rows": duplicates,
        "status": "Pass"
    }

    if missing > 0 or duplicates > 0:
        result["status"] = "Fail"
        logging.error(f"{name} failed validation")

    else:
        logging.info(f"{name} passed validation")

    validation_results.append(result)


try:
    logging.info("Starting validation step")

    region_summary = pd.read_csv("../data/aggregates/sales_by_region.csv")
    category_summary = pd.read_csv("../data/aggregates/sales_by_category.csv")
    monthly_summary = pd.read_csv("../data/aggregates/monthly_performance.csv")

    logging.info("All files loaded successfully")

    # Run validations
    validate_dataset(region_summary, "Region Summary")
    validate_dataset(category_summary, "Category Summary")
    validate_dataset(monthly_summary, "Monthly Summary")

except FileNotFoundError as e:
    logging.error(f"File not found: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")


# Save validation report
report_df = pd.DataFrame(validation_results)
report_df.to_csv("../data/validation/validation_report.csv", index=False)

logging.info("Validation process completed")