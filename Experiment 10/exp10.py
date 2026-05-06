import pandas as pd

# Load data (example CSV file)
df = pd.read_csv("data.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Check data info
print("\nData Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isna().sum())

# Clean data (remove missing values)
df = df.dropna()

# Explore data
print("\nStatistical Summary:")
print(df.describe())