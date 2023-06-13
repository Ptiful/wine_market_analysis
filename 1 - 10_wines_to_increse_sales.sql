-- - We want to highlight 10 wines to increase our sales, 
-- which ones should we choose and why?
SELECT ratings_average,ratings_count,name
FROM wines
WHERE ratings_average > 4.5 AND ratings_count > 30000
LIMIT 10;