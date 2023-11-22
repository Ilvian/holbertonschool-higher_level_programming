-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
