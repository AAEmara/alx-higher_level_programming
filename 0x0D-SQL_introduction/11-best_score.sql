-- Reading all records where score is bigger than or equal 10.
-- This query takes place in "second_table" table in "hbtn_0c_0".
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
