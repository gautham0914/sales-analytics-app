-- DAY 10: Views for Analytics (Video Game Sales Dataset)

-- View: Genre-wise Global Sales per Year

CREATE VIEW v_genre_yearly_sales AS
SELECT Year, Genre, SUM(Global_Sales) AS total_global_sales
FROM salesdb.sales_data
WHERE Year IS NOT NULL AND Genre IS NOT NULL
GROUP BY Year, Genre
ORDER BY Year, total_global_sales DESC;

select Year
from salesdb.sales_data sd 
