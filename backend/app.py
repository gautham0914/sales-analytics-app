from flask import Flask, jsonify
import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

app = Flask(__name__)

# Database Connection
def get_connection():
    conn = mysql.connector.connect(
        host="DB_HOST",
        user="DB_USER",
        password="DB_PASSWORD", 
        database="DB_NAME"
    )
    return conn


#  helps to  run a SQL query and convert to list of dicts in python 
#  which can be used in JSON 
def query_to_dicts(sql, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, params or ())
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()

    # turn each row into {"col": value}
    result = []
    for row in rows:
        result.append(dict(zip(cols, row)))
    return result


# ROUTES

@app.route("/")  
# WHEN SOMEONE VISITS URL(/), THIS TELLS FLASK TO RUN THE BELOW FUNCTION
def home():
    return jsonify({"message": " Sales Analytics API is running"})  # tells API is running


@app.route("/total-global-sales")
def total_global_sales():
    conn = get_connection()                                  # SQL CONNECTION
    cur = conn.cursor()                                      # TOOL TO RUN SQL COMMANDS
    cur.execute("SELECT SUM(Global_Sales) FROM sales_data;")
    result = cur.fetchone()[0]                               # RETURNS OUTPUT
    cur.close()
    conn.close()                                             # CLOSE SQL CONNECTION

    # result might be Decimal/None, so convert safely
    total = float(result) if result is not None else 0.0     # JSON only supports specific data types
    return jsonify({"total_global_sales": total})


@app.route("/top-games")
def top_games():
    """
    Top 10 games by total Global_Sales (across all rows).
    Groups by Name.
    """
    sql = """
        SELECT Name, SUM(Global_Sales) AS total_sales
        FROM sales_data
        GROUP BY Name
        ORDER BY total_sales DESC
        LIMIT 10;
    """
    data = query_to_dicts(sql)
    return jsonify(data)


@app.route("/sales-by-genre")
def sales_by_genre():
    """
    Total Global_Sales by Genre.
    """
    sql = """
        SELECT Genre, SUM(Global_Sales) AS total_sales
        FROM sales_data
        GROUP BY Genre
        ORDER BY total_sales DESC;
    """
    data = query_to_dicts(sql)
    return jsonify(data)


@app.route("/sales-by-platform")
def sales_by_platform():
    """
    Total Global_Sales by Platform.
    """
    sql = """
        SELECT Platform, SUM(Global_Sales) AS total_sales
        FROM sales_data
        GROUP BY Platform
        ORDER BY total_sales DESC;
    """
    data = query_to_dicts(sql)
    return jsonify(data)


@app.route("/yearly-sales")
def yearly_sales():
    """
    Total Global_Sales by Year.
    """
    sql = """
        SELECT Year, SUM(Global_Sales) AS total_sales
        FROM sales_data
        WHERE Year IS NOT NULL
        GROUP BY Year
        ORDER BY Year;
    """
    data = query_to_dicts(sql)
    return jsonify(data)

@app.route("/Publisher-sales", methods=["GET"])
def publisher_sales():
    """
    Total sales by publisher.
    """
    sql = """
        SELECT Publisher, SUM(Global_Sales) AS total_sales
        FROM sales_data
        WHERE Publisher IS NOT NULL
        GROUP BY Publisher
        ORDER BY total_sales;
    """
    data = query_to_dicts(sql)
    return jsonify(data)


#  Run this code only in main(app.py), and not when it's imported 
if __name__ == "__main__":
    # debug=True auto-restarts server when you change code (dev mode only)
    app.run(debug=True)
