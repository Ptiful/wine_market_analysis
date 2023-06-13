-- - We would like to do a selection of wines that are easy 
-- to find all over the world. **Find the top 3 most common 
-- `grape` all over the world** and **for each grape, give us 
-- the the 5 best rated wines**.

SELECT *
FROM grapes
JOIN most_used_grapes_per_country
ON grapes.id = most_used_grapes_per_country.grape_id
ORDER BY grape_id ASC
;

