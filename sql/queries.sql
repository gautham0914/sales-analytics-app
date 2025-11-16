
-- Video Game Sales Analytics Queries
-- Dataset: clean_sales.csv (Cleaned ETL-loaded MySQL table)
-- Project: Sales Analytics App 


-- 1. Calculate Total Global Sales
-- Purpose: Understand the overall size of the video game market.
-- Insight: Helps quantify industry scale in this dataset.
SELECT SUM(Global_Sales) AS total_global_sales
FROM sales_data;


-- 2. Top 10 Best-Selling Games
-- Purpose: Identify the most successful games ever.
-- Insight: Useful for analyzing what types of games dominate.
SELECT Name, Platform, Year, Genre, Global_Sales
FROM sales_data
ORDER BY Global_Sales DESC
LIMIT 10;



-- 3. Top 10 Genre with highest sales
-- Purpose: Rank genres based on total sales.
-- Insight: Helps understand customer preferences at a genre level.

SELECT Genre, SUM(Global_Sales) AS revenue
FROM sales_data
GROUP BY Genre
ORDER BY revenue DESC;



-- 4. Top 10 Platform with highest sales
-- Purpose: Measure which consoles/platforms sell the most.
-- Insight: Shows which gaming systems are most profitable.
SELECT Platform, SUM(Global_Sales) AS revenue
FROM sales_data
GROUP BY Platform
ORDER BY revenue DESC;



-- 5. Top 10 years with highest sales
-- Purpose: Analyze how video game sales evolved across years.
-- Insight: Identifies growth/decline periods in gaming history.
SELECT Year, SUM(Global_Sales) AS yearly_sales
FROM sales_data
GROUP BY Year
ORDER BY Year;


-- 6. Top 10 Publishers with highest sales
-- Purpose: Find the companies generating the most revenue.
-- Insight: Shows which publishers dominate the market.
SELECT Publisher, SUM(Global_Sales) AS publisher_revenue
FROM sales_data
GROUP BY Publisher
ORDER BY publisher_revenue DESC
LIMIT 10;


-- 7 Regional Sales
-- Purpose: Compare performance across NA, EU, JP, Other.
-- Insight: Shows which region contributes the most revenue.
SELECT 
    SUM(NA_Sales) AS Total_NA,
    SUM(EU_Sales) AS Total_EU,
    SUM(JP_Sales) AS Total_JP,
    SUM(Other_Sales) AS Total_Other,
    SUM(Global_Sales) AS Total_Global
FROM sales_data;

-- 8. Publishers with the Most Games Released
-- Purpose: Identify companies with the largest product catalog.
-- Insight: High output publishers may dominate market share.
SELECT Publisher, COUNT(*) AS num_games
FROM sales_data
GROUP BY Publisher
ORDER BY num_games DESC
LIMIT 10;
