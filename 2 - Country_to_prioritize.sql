-- We have a marketing budget for this year, 
-- which country should we prioritise and why?
SELECT name,wines_count /SUM(users_count) 
FROM countries
ORDER BY wines_count ASC;