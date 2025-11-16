import pandas as pd

df = pd.read_csv('data/sales_analyst.csv')
print(df.shape)
print(df.head())
print(df.columns)
#check for null values 
df.isnull().sum()
df.head()