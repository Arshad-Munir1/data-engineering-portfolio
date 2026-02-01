import pandas as pd

input_file = "../data/superstore_raw.csv"
output_file = "../data/superstore_clean.csv"

df = pd.read_csv(input_file, encoding="latin1")

print("Dataset loaded successfully")

#standardise column names
df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ","_")
)
print("Column names cleaned")

#convert date columns
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
print("Date columns converted")

# Create profit margin column
df["profit_margin"] = (df["profit"] / df["sales"]) * 100
print("Profit margin created")

# Round financial columns
df["sales"] = df["sales"].round(2)
df["profit"] = df["profit"].round(2)
df["profit_margin"] = df["profit_margin"].round(2)
print("Financial Values Rounded")

#Save cleaned dataset
df.to_csv(output_file, index=False)
print("Clean dataset saved successfully")

#Reload for validation
df = pd.read_csv(output_file, encoding="latin1", parse_dates=["order_date", "ship_date"])
print(df.info())