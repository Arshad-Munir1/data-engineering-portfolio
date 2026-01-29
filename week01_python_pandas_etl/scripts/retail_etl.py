import pandas as pd

# File paths
input_file = "../data/superstore_raw.csv"
output_file = "../data/superstore_clean.csv"

# Extract
print("Loading dataset...")
df = pd.read_csv(input_file)

# Transform
print("Cleaning data...")

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Handle missing values
df.fillna(0, inplace=True)

# Create revenue column if sales exists
if "sales" in df.columns:
    df["revenue"] = df["sales"]

# Load
print("Saving cleaned dataset...")
df.to_csv(output_file, index=False)

print("ETL process completed successfully!")