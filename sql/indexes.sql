-- Indexes 

-- Faster search grouping by game name
USE salesdb;
CREATE INDEX idx_name ON salesdb.sales_data(Name);


CREATE INDEX idx_platform
ON salesdb.sales_data(Platform);

CREATE INDEX idx_year
ON salesdb.sales_data(Year);

CREATE INDEX idx_genre
ON salesdb.sales_data(Genre);

CREATE INDEX idx_publisher
ON salesdb.sales_data(Publisher);

CREATE INDEX idx_na_sales
ON salesdb.sales_data(NA_Sales);

CREATE INDEX idx_eu_sales
ON salesdb.sales_data(EU_Sales);

CREATE INDEX idx_jp_sales
ON salesdb.sales_data(JP_Sales);

CREATE INDEX idx_other_sales
ON salesdb.sales_data(Other_Sales);

CREATE INDEX idx_global_sales
ON salesdb.sales_data(Global_Sales);


