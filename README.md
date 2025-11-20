# Sales Analytics App

Building an end-to-end Sales Analytics App in 14 days.

## Day 1 – Setup
- Installed tools  
- Created folder structure  
- Added dataset  
- Published to GitHub  

Dataset: data/sales_analyst.csv

## Day 2 — Data Cleaning (ETL)

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



## Day 3 — SQL Database Integration & Analysis

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


## Day 4 - Automated ETL Pipeline (Python → MySQL + Logging)

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

- etl/pipeline.py → Master ETL + load script

- log/pipeline.log → Log file showing timestamps & operations

- Updated .gitignore to ignore log files

### How to run the pipeline
- python3 etl/pipeline.py

### Example log output (from pipeline.log)
2025-11-17 12:41:39 - INFO - 🚀 Pipeline started

2025-11-17 12:41:39 - INFO - Loaded 16327 rows and 11 columns.

2025-11-17 12:41:39 - INFO - Connecting to MySQL...

2025-11-17 12:41:40 - INFO - Inserted 16327 rows successfully.

2025-11-17 12:41:40 - INFO - Pipeline finished in 0.95 seconds

## Day 5 – Flask API + MySQL Integration (Backend Layer)
### Goal

Build a working backend API using Flask that connects to MySQL and returns live game-sales data through JSON endpoints.

### What I built

- A Flask backend (backend/app.py) that:

- Connects to the MySQL salesdb database

- Reads data from the games_sales table

- Returns clean JSON output

- Handles CORS so dashboards/tools can use the API

- Runs on port 5000

- A database connector file (backend/db.py) that:

- Stores database connection settings

- Creates a reusable MySQL connection for the API

Verified the database contains all columns with correct spellings:
Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales

- Endpoints created

1. /top-games
Returns the top games ordered by Global_Sales.

2. Check
Optional: simple root route to confirm server is running.

### What the backend now does

- Converts SQL query results → JSON for frontend or dashboards

- Provides real-time access to the dataset via API

- Allows future dashboards (React, Streamlit, Tableau API, etc.) to pull fresh data

- Fully replaces manual CSV loading in frontend

- Works directly with the cleaned + automated ETL pipeline from Day 4

### Why this is important

- Every modern analytics app uses an API layer to serve data

- Makes the project production-ready

- External tools (React, Python scripts, Power BI, Tableau, etc.) can now consume your data

- API ensures the backend is decoupled from the database

- Enables future endpoints: yearly stats, platform trends, genre insights, etc.

### Files created today

- backend/app.py → Main Flask API service

- backend/db.py → MySQL database connector

Updated requirements.txt with Flask, mysql-connector-python, flask-cors

### How to run the backend
cd backend

python app.py


### Then open:
http://127.0.0.1:5000/top-games

Example API output (from /top-games)
[
  {
    "Rank": 1,
    "Name": "Wii Sports",
    "Platform": "Wii",
    "Year": 2006,
    "Genre": "Sports",
    "Publisher": "Nintendo",
    "NA_Sales": 41.36,
    "EU_Sales": 28.96,
    "JP_Sales": 3.77,
    "Other_Sales": 8.65,
    "Global_Sales": 82.74
  }
]

### Status

Backend layer is now complete.
API is live and successfully connected to MySQL.


## Day 6 – Tableau Dashboard + Public Link

### Goal

Create an interactive Tableau dashboard using the MySQL database and publish it online for easy access.

### What I built

- Connected Tableau to the salesdb MySQL database

- Built multiple visualizations:

- Yearly sales trend

- Top games

- Sales by region

- Sales by genre

- Platform and publisher performance

- Combined all visuals into one clean dashboard

- Published the dashboard to Tableau Public

- Added the link + screenshot to the /dashboard folder

### Why this is important

- Shows BI/visualization skills

- Demonstrates end-to-end analytics workflow:
  ETL → MySQL → Tableau

### Files created today

- dashboard/Dashboard.png → Screenshot

- dashboard/tableau_link.txt → Public link

### How to publish

- Server → Tableau Public → Save to Tableau Public

- Log in and save

- Copy the public link

- Paste it into dashboard/tableau_link.txt

### How to view

- Open the Tableau link or the screenshot inside /dashboard.

### Status

Tableau analytics layer is complete and live.

 ## DAY 7 — Bug Fixing, Optimization & Project Cleanup
 ### Goal

Stabilize the entire project, fix issues, clean the repository, and make sure all layers (ETL → MySQL → API → Tableau) work smoothly.

### What I Completed Today
- Bug Fixing Across ETL, API & Dashboard

- Verified all Flask endpoints:
  /top-games, /sales-by-platform, /sales-by-region

- Fixed file path issues in ETL pipeline.

- Restarted and cleared port conflicts for Flask server.

- Confirmed cleaned dataset loads correctly into MySQL.

### ETL Pipeline Validation

- Ran pipeline.py successfully.

- Confirmed clean data loads into MySQL without errors.

- Verified correct row count, column names, and datatypes.

### Repository Cleanup

- Removed unused/backup files.

- Organized folders: backend/, etl/, dashboard/, sql/, data/.

- Ensured clean folder structure with only necessary files.

- Updated .gitignore to avoid logging clutter.

### Tableau Dashboard Integration Review

- Confirmed Tableau connected properly to MySQL extract.

- Verified all dashboard sheets update correctly.

- Ensured published dashboard link is stored in dashboard/tableau_link.txt.

- Added clean screenshot inside dashboard/.

### Day 7 Status

 Everything is clean, optimized, tested, and stable.
 The full workflow ETL → MySQL → API → Tableau is working end-to-end.

## DAY 8 — System Design + Documentation (Tableau Edition)

### Goal
Document the full data pipeline, create the architecture diagram, organize Tableau assets, and make the repository clean and interview-ready.

### Tasks Completed

### 1. Created Architecture Diagram
A Tableau-centric system design diagram was created and saved at:
docs/architecture_diagram.png

Data Flow:
sales_analyst.csv → ETL → clean_sales.csv → MYSQL → (API optional) → Tableau Dashboard

This shows the complete end-to-end pipeline in a single visual.

### 2. Organized Tableau Assets
Created a new folder:
tableau/

Added the following files:
- dashboard.twbx
- dashboard_screenshot.png
- tableau_public_link.txt

This keeps all Tableau-related items in one place.

### 3. Updated README (Pipeline + Tableau Instructions)
Added sections explaining:
- Project overview
- Architecture diagram
- Tools used (Python, pandas, PostgreSQL, Flask, Tableau)
- How Tableau connects to PostgreSQL
- How the dashboard was published to Tableau Public
- Screenshot of the dashboard

### 4. Documented API Endpoints
Added clear descriptions for:
- /revenue
- /top-products
- /sales-by-region
- /monthly-revenue

These show the analytical API layer of the project.

### 5. Added “How to Run This Project” Section
Documented steps for:
- cloning the repo
- installing dependencies
- running the ETL
- running the API
- connecting Tableau to PostgreSQL
- publishing to Tableau Public
### Files Added/Updated
- docs/architecture_diagram.png
- tableau/dashboard.twbx
- tableau/dashboard_screenshot.png
- tableau/tableau_public_link.txt
- README.md (architecture, Tableau instructions, API documentation)
### Summary
Day 8 focused on documentation, system design, and making the project look complete and professional. The architecture diagram, Tableau assets, and updated README provide a clear overview of the entire pipeline for recruiters and technical reviewers.
## DAY 9 — SECURITY (Environment Variables + Password Hashing + Secrets Management)

### Goal
Secure the project by removing hard-coded passwords, using environment variables, protecting secrets from GitHub, and adding a simple password hashing demonstration.

### Tasks Completed

### 1. Added .env for local secrets
Created a `.env` file (not uploaded to GitHub) to store:
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_PORT

This keeps real credentials out of the codebase.

### 2. Implemented python-dotenv
Both `etl/pipeline.py` and `backend/app.py` were updated to use:
- load_dotenv()
- os.getenv()

All database connections now pull values from environment variables instead of plain text.

### 3. Updated .gitignore
Added entries to prevent sensitive or unnecessary files from being committed:
.env
log/
pycache/
*.pyc

diff
Copy code

### 4. Added .env.example
Created a template file (`.env.example`) containing placeholder values so anyone cloning the repo knows which variables to create.

### 5. Added a password hashing demo
- Created `security/hash_demo.py` to demonstrate:
- hashing a password using bcrypt
- verifying correct vs wrong passwords
- understanding hashing and salting basics

### Files Added/Updated
- .env.example
- .gitignore
- backend/app.py (dotenv integration)
- etl/pipeline.py (dotenv integration)
- security/hash_demo.py

### Summary
**Day 9 adds essential security practices:**
- secrets removed from all Python files
- environment variables implemented correctly
- sensitive files ignored by Git
- example env template added for safe sharing
- hashing fundamentals demonstrated for interviews

