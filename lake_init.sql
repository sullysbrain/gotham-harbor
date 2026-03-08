ATTACH 'ducklake:retail.ducklake' AS retail_lake
(DATA_PATH 'retail_data/');

USE retail_lake;

-- Optional: confirm what's loaded
SHOW ALL TABLES;
