import mysql.connector
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT"))


def load_to_db(df):
    """Loads a cleaned DataFrame into MySQL"""

    logging.info("Connecting to MySQL...")

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )
    cur = conn.cursor()

    logging.info("Recreating table sales_data...")

    cur.execute("DROP TABLE IF EXISTS sales_data")

    cur.execute("""
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
        )
    """)

    insert_sql = """
        INSERT INTO sales_data
        (`Rank`, `Name`, `Platform`, `Year`, `Genre`, `Publisher`,
         `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    rows = [
        (
            int(row['Rank']),
            row['Name'],
            row['Platform'],
            int(row['Year']) if row['Year'] == row['Year'] else None,
            row['Genre'],
            row['Publisher'],
            float(row['NA_Sales']),
            float(row['EU_Sales']),
            float(row['JP_Sales']),
            float(row['Other_Sales']),
            float(row['Global_Sales'])
        )
        for _, row in df.iterrows()
    ]

    cur.executemany(insert_sql, rows)
    conn.commit()

    logging.info(f"✅ Inserted {cur.rowcount} rows into MySQL.")

    cur.close()
    conn.close()

    logging.info("✅ load_to_db() completed successfully")

