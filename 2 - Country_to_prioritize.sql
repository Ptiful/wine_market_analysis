-- We have a marketing budget for this year, 
-- which country should we prioritise and why?
SELECT name,wines_count *1.0  / (users_count)  AS something
FROM countries
ORDER BY something;