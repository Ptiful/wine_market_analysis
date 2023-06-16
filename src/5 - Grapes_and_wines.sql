-- - We would like to do a selection of wines that are easy 
-- to find all over the world. **Find the top 3 most common 
-- `grape` all over the world** and **for each grape, give us 
-- the the 5 best rated wines**.
-- SELECT Type, COUNT(*) FROM TABLE GROUP BY Type
SELECT COUNT(grapes.id) AS grape_id, grapes.name, country_code, wines_count
FROM grapes
JOIN most_used_grapes_per_country
ON grapes.id = most_used_grapes_per_country.grape_id
GROUP BY name
ORDER BY grape_id DESC
;

