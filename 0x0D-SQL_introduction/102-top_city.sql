-- -- display top 3 of cities temperature during july and august order by temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;