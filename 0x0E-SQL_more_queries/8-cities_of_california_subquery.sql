-- This scripts lists all the cities of californa found
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id
