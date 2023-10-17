-- Reading the records with the same score in "second_table".
SELECT score, COUNT(score)
FROM second_table
GROUP BY score;
