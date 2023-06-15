--We would to give create a country leaderboard,
--give us a visual that shows the **average wine 
--rating for each country`**. Do the same for 
---the `vintages`.
SELECT AVG(wines.ratings_average) AS averaging_wine_rating_average, regions.country_code
FROM wines
JOIN regions
ON wines.region_id = regions.id
GROUP BY country_code
order by AVG(wines.ratings_average) DESC;