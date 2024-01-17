-- LIST ALL CITES OF CALIFORNIA THE BE FOUND ON hbtn_0d_usa
-- THE states CONTAINE ONE RECORD name = California
-- OREDER BY cities.id
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
);