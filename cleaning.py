import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Convert date column to datetime format
df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check data types
print("\nData Types:\n")
print(df.dtypes)

# Check missing values
print("\nMissing Values Before Cleaning:\n")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values with mean
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values with mode
for column in df.select_dtypes(include=['object', 'string']).columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Check missing values after cleaning
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")