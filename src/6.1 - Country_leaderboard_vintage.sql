SELECT countries.name , AVG(vintage_toplists_rankings.rank) AS average_vintage_topliste_rankings
FROM vintages
JOIN vintage_toplists_rankings
ON vintages.id = vintage_toplists_rankings.vintage_id
JOIN toplists
ON vintage_toplists_rankings.top_list_id = toplists.id
JOIN countries
ON toplists.country_code =  countries.code
GROUP BY countries.name
ORDER BY AVG(vintage_toplists_rankings.rank) DESC;