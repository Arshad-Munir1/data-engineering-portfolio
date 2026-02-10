import pandas as pd
import os

# Ensure validation directory exists
os.makedirs("../data/validation", exist_ok=True)

#Load aggregated data

region_summary = pd.read_csv("../data/aggregates/sales_by_region.csv")
category_summary = pd.read_csv("../data/aggregates/sales_by_category.csv")
monthly_summary = pd.read_csv("../data/aggregates/monthly_performance.csv")

# Create validation report
checks = []

def run_checks(df, name):
    checks.append({
        "dataset": name,
        "check": "missing_values",
        "result": df.isnull().sum().sum()
    })
    checks.append({
        "dataset": name,
        "check": "duplicates",
        "result": df.duplicated().sum()
    })

run_checks(region_summary, "region_summary")
run_checks(category_summary, "category_summary")
run_checks(monthly_summary, "monthly_summary")

validation_report = pd.DataFrame(checks)

# Save validation report
validation_report.to_csv(
    "../data/validation/validation_report.csv",
    index=False
)

print("Validation report saved successfully")
print(validation_report)