-- LIST ALL CITIES 
-- DIPLAY cities.id - cities.name - states.name
-- order cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id