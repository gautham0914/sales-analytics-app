import pandas as pd
import mysql.connector

# 1. Read the cleaned CSV
path = 'data/clean_sales.csv'
df = pd.read_csv(path)

print("CSV loaded. Shape:", df.shape)
print(df.head(3))

# 2. Connect Python → MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gautham@123", 
    database="salesdb",
    port=3306
)
cur = conn.cursor()

# 3. Drop old table and recreate
cur.execute("DROP TABLE IF EXISTS sales_data")

create_table_sql = """
CREATE TABLE sales_data (
    `Rank` INT,
    `Name` VARCHAR(255),
    `Platform` VARCHAR(50),
    `Year` INT,
    `Genre` VARCHAR(50),
    `Publisher` VARCHAR(100),
    `NA_Sales` FLOAT,
    `EU_Sales` FLOAT,
    `JP_Sales` FLOAT,
    `Other_Sales` FLOAT,
    `Global_Sales` FLOAT,
    id INT AUTO_INCREMENT PRIMARY KEY
);
"""
cur.execute(create_table_sql)
print("Table created successfully.")

#4. Prepare INSERT statement
insert_sql = """
INSERT INTO sales_data
(`Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`,
 `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# 5. Convert DataFrame → list of tuples
rows = []
for _, row in df.iterrows():
    rows.append((
        int(row['Rank']),
        row['Name'],
        row['Platform'],
        int(row['Year']),
        row['Genre'],
        row['Publisher'],
        float(row['NA_Sales']),
        float(row['EU_Sales']),
        float(row['JP_Sales']),
        float(row['Other_Sales']),
        float(row['Global_Sales']),
    ))

# 6. Insert all rows
cur.executemany(insert_sql, rows)
conn.commit()

print(f"Inserted {cur.rowcount} rows into MySQL.")

# 7. Close connections
cur.close()
conn.close()
print("Done.")

conn = mysql.connector.connect
