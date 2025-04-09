import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)

# Basic operations
print(df.head())  # Show first few rows

print("""###########################""")

print(df.describe())  # Summary statistics

print("""###########################""")

print(df[df['Age'] > 25])  # Filtering data

# Save and load CSV
df.to_csv('sample_data.csv', index=False)
df_loaded = pd.read_csv('sample_data.csv')

print("\nLoaded Data:\n", df_loaded)