import pandas as pd
import os

# Ensure validation directory exists
os.makedirs("../data/validation", exist_ok=True)

#Load aggregated data

region_summary = pd.read_csv("../data/aggregates/sales_by_region.csv")
category_summary = pd.read_csv("../data/aggregates/sales_by_category.csv")
monthly_summary = pd.read_csv("../data/aggregates/monthly_performance.csv")

# Create validation report
validation_results = []

def validate_dataset(df, name):

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    validation_results.append({
        "dataset": name,
        "missing_values": missing,
        "duplicates": duplicates
    })

    # Hard stops
    assert missing == 0, f"{name} contains missing values"
    assert duplicates == 0, f"{name} contains duplicates"

    print(f"{name} passed validation ✅")


validate_dataset(region_summary, "Region Summary")
validate_dataset(category_summary, "Category Summary")
validate_dataset(monthly_summary, "Monthly Summary")

# Save report
report_df = pd.DataFrame(validation_results)
report_df.to_csv("../data/validation/validation_report.csv", index=False)

print("Validation report saved.")
print("All datasets passed validation 🎉")