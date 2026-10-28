-- Write your PostgreSQL query statement below
SELECT e.name, b.bonus
FROM Employee as e
LEFT JOIN Bonus as b using (empId)
WHERE b.bonus < 1000 OR b.bonus IS NULL;