-- - We has detected that a big cluster of customers like a 
-- specific combination of tastes. We have identified few `primary`
--  `keywords` that matches this and we would like you to *
-- *find all the wines that have those keywords**. 
-- To ensure accuracy of our selection, ensure that **more than 
-- 10 users confirmed those keywords**. Also, identify the 
-- `flavor_groups` related to those keywords.
-- 	- Coffee
-- 	- Toast
-- 	- Green apple
-- 	- cream 
-- 	- citrus

SELECT wines.*
FROM wines
JOIN keywords_wine
ON wines.id = keywords_wine.wine_id
-- FROM keywords_wine
JOIN keywords
ON keywords_wine.keyword_id =  keywords.id
WHERE keywords_wine.count > 10 
AND keywords.name 
IN ('Coffee','Toast','Green apple','cream','citrus');