import pandas as pd

# Step 1: Read dataset
data = pd.read_csv("data.csv")

# Step 2: Display all columns (features)
print("Features (Columns) in Dataset:")
print(list(data.columns))

# Step 3: Select numeric columns
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# Step 4: Calculate descriptive statistics
print("\nDescriptive Statistics:\n")

print("Count:\n", numeric_data.count())
print("\nMean:\n", numeric_data.mean())
print("\nMedian:\n", numeric_data.median())
print("\nMaximum:\n", numeric_data.max())
print("\nMinimum:\n", numeric_data.min())
print("\nVariance:\n", numeric_data.var())
print("\nStandard Deviation:\n", numeric_data.std())