-- One of our VIP client likes `Cabernet Sauvignon`
--, he would like a top 5 recommandation, 
--which wines would you recommend to him?

SELECT id, name, AVG(acidity), AVG(fizziness), AVG(intensity), AVG(sweetness), AVG(tannin)
FROM wines
WHERE name LIKE 'Cabernet Sauvignon';

SELECT id, name, acidity, intensity, sweetness, tannin
FROM wines
WHERE name NOT LIKE 'Cabernet Sauvignon'
AND acidity BETWEEN 3 AND 4
AND intensity BETWEEN 4 AND 5
AND sweetness  BETWEEN 1.7 AND 2
AND tannin  BETWEEN 3 AND 4
LIMIT 5;