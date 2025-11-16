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
Dataset is now fully analyzed and ready for **Day 4: Dashboards**.
