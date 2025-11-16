
-- Video Game Sales Analytics Queries
-- Dataset: clean_sales.csv (Cleaned ETL-loaded MySQL table)
-- Project: Sales Analytics App 

-- 1. Calculate Total Global Sales
-- Purpose: Understand the overall size of the video game market.
-- Insight: Helps quantify industry scale in this dataset.
SELECT SUM(Global_Sales) AS total_global_sales
FROM sales_data;




