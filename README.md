# Sales Analytics App

Building an end-to-end Sales Analytics App in 14 days.

**Day 1 – Setup**
- Installed tools  
- Created folder structure  
- Added dataset  
- Published to GitHub  

Dataset: data/sales_analyst.csv


**Day 2 — Data Cleaning (ETL)**

**Goal:** Prepare raw sales data for analysis by cleaning and standardizing it.

### ✔ Tasks Completed
- Loaded the raw dataset (`sales_analyst.csv`)
- Handled missing values:
- Filled null publishers with `"Unknown"`
- Dropped rows with missing `Year`
- Converted numeric columns to correct data types
- Removed duplicates
- Cleaned and standardized column names
- Exported final cleaned dataset → `data/clean_sales.csv`

### 📂 Files Created/Updated
- `etl/transform.py` — Python ETL script  
- `etl/transform_backup.ipynb` — Notebook version of the ETL  
- `data/clean_sales.csv` — Final cleaned dataset  

### Output Summary
The dataset is fully cleaned and ready for loading into SQL (Day 3).



**Day 3 — SQL Database Integration & Analysis**

**Goal:** Load the cleaned dataset into MySQL and perform SQL-based analysis.

### ✔ Tasks Completed
- Created MySQL database: `salesdb`
- Created table: `sales_data`
- Loaded cleaned CSV into MySQL using `etl/load_to_db.py`
- Verified loading using DBeaver
- Wrote and executed analytical SQL queries

### Files Created/Updated
- `etl/load_to_db.py` — Python script to load CSV → MySQL
- `sql/queries.sql` — Contains all analytical SQL queries
- `SQL-Outputs/` — Folder with screenshots of SQL results

### Key SQL Insights Included
- Total global sales
- Top 10 best-selling games (grouped by total franchise sales)
- Sales by genre
- Sales by platform
- Top-selling game per platform
- Yearly sales trends
- Regional revenue comparison
- Most profitable genres over time

### Status
SQL layer is complete.  
Dataset is now fully analyzed and ready.


**Day 4 - Automated ETL Pipeline (Python → MySQL + Logging)**

### Goal 
Automate the entire ETL + Database refresh process so the dataset can be cleaned and loaded into MySQL automatically at any time. 

### What I built

- A pipeline script (etl/pipeline.py) that:

- Loads the cleaned CSV

- Connects to MySQL

- Drops the old table

- Recreates the table

- Inserts all rows

- Writes run logs to log/pipeline.log

### What the pipeline does

- Ensures the database always has the fresh, clean version of the dataset

- Makes the ETL process repeatable with one command

- Logs every action (start time, end time, row count, errors)

- Replaces manual SQL imports with a fully automated workflow

### Why automation is important

- Real-world companies don’t load data manually

- Automated ETL makes the project production-ready

- You can schedule it to run every hour/day

- Ensures the DB is always up-to-date

- Useful when dashboards depend on live data

### Files created today

etl/pipeline.py → Master ETL + load script

log/pipeline.log → Log file showing timestamps & operations

Updated .gitignore to ignore log files

### How to run the pipeline
python3 etl/pipeline.py

### Example log output (from pipeline.log)
2025-11-17 12:41:39 - INFO - 🚀 Pipeline started

2025-11-17 12:41:39 - INFO - Loaded 16327 rows and 11 columns.

2025-11-17 12:41:39 - INFO - Connecting to MySQL...

2025-11-17 12:41:40 - INFO - Inserted 16327 rows successfully.

2025-11-17 12:41:40 - INFO - Pipeline finished in 0.95 seconds


