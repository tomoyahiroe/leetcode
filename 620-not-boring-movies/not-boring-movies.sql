-- Write your PostgreSQL query statement below
SELECT id, movie, description, ROUND(rating,2) AS rating
FROM Cinema
WHERE id % 2 = 1 AND NOT description = 'boring'
ORDER BY rating DESC;