-- Write your PostgreSQL query statement below
SELECT user_id, ROUND(COALESCE(confirmation_rate,0),2) AS confirmation_rate
FROM Signups
LEFT JOIN (
    SELECT user_id, AVG(CASE WHEN action = 'confirmed' THEN 1.0 ELSE 0.0 END) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
) using (user_id);