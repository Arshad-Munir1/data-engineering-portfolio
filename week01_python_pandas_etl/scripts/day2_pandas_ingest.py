import pandas as pd

#Load dataset
file_path = "../data/superstore_raw.csv"
df = pd.read_csv(file_path, encoding="latin1")

#preview data
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

#Check for missing values
print("\nMissing Values per Coulumn:")
print(df.isnull().sum())