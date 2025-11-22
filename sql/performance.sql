
USE salesdb;

-- EXPLAIN ANALYZE

SELECT Platform , SUM(Global_Sales)
FROM salesdb.sales_data
GROUP BY Platform;

-- BEFORE INDEXING, EXECUTION TIMES

--Query 1 — GROUP BY Platform
actual time = 30.8 ms
rows = 31
plan = Table scan on <temporary> → Aggregate

-- Query 2 — WHERE Genre = 'Sports'
actual time = 15.1 ms
rows ≈ 2304
plan = Filter (full table scan)

-- Query 3 — ORDER BY Global_Sales DESC
actual time = 17.5 ms
rows ≈ 16327
plan = Sort on Global_Sales (full scan + sort)




-- Query 1 — GROUP BY Platform
actual time = 16.68 ms
rows = 31
plan = Index-assisted aggregate
-- IMPROVEMENT
(30.8 - 16.68) / 30.8 x 100 ≈ 45.8% faster


-- Query 2 — WHERE Genre = 'Sports'
actual time = 5.73 ms
rows ≈ 2304
plan = Index lookup using idx_genre
-- IMPROVEMENT
(15.1-5.73)/15.1x100≈62.05%


---- Query 3 — ORDER BY Global_Sales DESC
actual time = 15.6 ms
rows ≈ 16327
plan = Still sorting (index not yet used for ORDER BY)
--IMPROVEMENT
(17.5 - 15.6) / 17.5 x 100 ≈ 10.8% faster


--  Your ORDER BY query did NOT fully optimize because MySQL only uses indexes for sorting if the index order matches
-- TO FIX 
CREATE INDEX idx_global_sales_desc
ON salesdb.sales_data(Global_Sales DESC);

EXPLAIN ANALYZE
SELECT Name, Global_Sales
FROM salesdb.sales_data
ORDER BY Global_Sales DESC
LIMIT 10;




