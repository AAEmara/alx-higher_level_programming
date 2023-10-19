-- Reading all cities contained in "hbtn_0d_usa".
SELECT cities.id, cities.name, states.name
FROM states
JOIN cities
ON states.id = cities.state_id
ORDER BY cities.id;
