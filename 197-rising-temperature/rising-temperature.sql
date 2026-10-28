-- Write your PostgreSQL query statement below
SELECT l.id
FROM Weather as l
LEFT JOIN Weather as r on l.recordDate = r.recordDate + interval '1 days'
WHERE l.temperature > r.temperature;