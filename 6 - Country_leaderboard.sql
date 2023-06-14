--We would to give create a country leaderboard,
--give us a visual that shows the **average wine 
--rating for each country`**. Do the same for 
---the `vintages`.
SELECT AVG(wines.ratings_average), regions.country_code
FROM wines
JOIN regions
ON wines.region_id = regions.id
GROUP BY country_code
order by AVG(wines.ratings_average) DESC;

-- SELECT AVG(vintages.ratings_average), regions.country_code
-- FROM vintages
-- JOIN regions
-- ON vintages.region_id = regions.id
-- GROUP BY country_code
-- order by AVG(wines.ratings_average) DESC;
SELECT countries.name , AVG(vintage_toplists_rankings.rank)
FROM vintages
JOIN vintage_toplists_rankings
ON vintages.id = vintage_toplists_rankings.vintage_id
JOIN toplists
ON vintage_toplists_rankings.top_list_id = toplists.id
JOIN countries
ON toplists.country_code =  countries.code
GROUP BY countries.name
ORDER BY AVG(vintage_toplists_rankings.rank);