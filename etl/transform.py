import pandas as pd

df = pd.read_csv('/Users/gauthamgongada/Desktop/sales-analytics-app/data/sales_analyst.csv')
print(df.shape)
print(df.head())
print(df.columns)
#check for null values 
df.isnull().sum()
df.head()

df.isnull().sum()
df.head(5)

# Delete duplicate rows
df = df.drop_duplicates()

# Check Data Types
df.dtypes

df.info

df = df.dropna(how='all') #drops the rows which are completely empty

df.shape

df['Publisher'] = df['Publisher'].fillna('Unknown')

df = df.dropna()


df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
# converts year column to int numeric and "coerce" is helpfull when valued cant be convertd to numeric it wont throw error
df['Year'] = df['Year'].astype('Int64')

df.isnull().sum()


# Ensure sales columns are numeric
sales_cols = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

for col in sales_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    else:
        print(f"Warning: expected sales column '{col}' not found in data.")

print("\nDtypes after numeric conversion:\n", df.dtypes)



print("\nNull counts per column:\n", df.isnull().sum())
print("\nPreview of cleaned data:\n", df.head())



#Save cleaned dataset
output_path = '../data/clean_sales.csv'
df.to_csv(output_path, index=False)
print(f"\n Clean file saved successfully to {output_path}")
print("Final shape:", df.shape)



df['Name'].value_counts()