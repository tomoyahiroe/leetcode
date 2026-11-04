-- Write your PostgreSQL query statement below
SELECT project_id, ROUND(AVG(experience_years * 1.0), 2) AS average_years
FROM Employee
INNER JOIN Project using (employee_id)
GROUP BY project_id;