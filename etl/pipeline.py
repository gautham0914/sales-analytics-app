#Imports (Libraries we need)
import pandas as pd
import mysql.connector
import logging
import time
from transform import transform_data
from load_to_db import load_to_db

#for python to read .env file for credentials
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")



# Create a log file to track each pipeline run
logging.basicConfig(
    filename="/Users/gauthamgongada/Desktop/sales-analytics-app/log/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_clean_data():
    logging.info("Loading clean_sales.csv ...")
    df = pd.read_csv("/Users/gauthamgongada/Desktop/sales-analytics-app/data/clean_sales.csv")
    logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    return df


# Load Data into MySQL

def load_to_mysql(df):
    logging.info("Connecting to MySQL...")

    conn = mysql.connector.connect(
        host="DB_HOST",
        user="DB_USER",
        password="DB_PASSWORD", 
        database="DB_NAME"
    )
    cur = conn.cursor()

    logging.info("Recreating table sales_data...")

    cur.execute("DROP TABLE IF EXISTS sales_data")

    cur.execute("""
        CREATE TABLE sales_data (
           `Rank` INT,
            Name VARCHAR(255),
            Platform VARCHAR(50),
            Year INT,
            Genre VARCHAR(50),
            Publisher VARCHAR(255),
            NA_Sales FLOAT,
            EU_Sales FLOAT,
            JP_Sales FLOAT,
            Other_Sales FLOAT,
            Global_Sales FLOAT
        )
    """)

    logging.info("Inserting rows...")

    insert_sql = """
        INSERT INTO sales_data 
            (`Rank`, Name, Platform, Year, Genre, Publisher,
             NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cur.executemany(insert_sql, df.values.tolist())
    conn.commit()

    logging.info(f"Inserted {cur.rowcount} rows successfully.")

    cur.close()
    conn.close()

# Run Full Pipeline
def run_pipeline():
    start = time.time()
    logging.info("🚀 Pipeline started")

    df = load_clean_data()
    load_to_mysql(df)

    end = time.time()
    duration = round(end - start, 2)
    logging.info(f"Pipeline finished in {duration} seconds")

def run_pipeline():
    try:
        logging.info("🚀 Pipeline started")
        df = transform_data()
        load_to_db(df)
        logging.info(f"✅ Data loaded successfully — {df.shape[0]} rows")

        logging.info("✅ Pipeline finished successfully")
    except Exception as e:
        logging.error(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()


