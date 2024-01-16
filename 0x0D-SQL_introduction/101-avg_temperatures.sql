-- import hbtn_0c_0 database this table dump
-- display average temperature by city
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;