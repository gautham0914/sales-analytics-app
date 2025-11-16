import pandas as pd

# Step 1: Read the real dataset
df = pd.read_csv('sales_analyst.csv')
print("Shape:", df.shape)
print(df.head())
print(df.columns)
