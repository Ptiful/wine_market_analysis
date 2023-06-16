-- - We would like to give a price to the best winery, 
-- which one should we choose and why?
SELECT wineries.*, MAX(wines.ratings_average) / SUM(wines.ratings_count)
FROM wineries
INNER JOIN wines ON wineries.id = wines.winery_id;
