-- List all rows in the score name group
SELECT score, name
FROM second_table
WHERE name <> ""
ORDER BY score DESC
