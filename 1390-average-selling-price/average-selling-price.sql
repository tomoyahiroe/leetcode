-- Write your PostgreSQL query statement below
SELECT 
    p.product_id, 
    COALESCE(
        ROUND(
            SUM(price * units)*1.0/NULLIF(SUM(units)*1.0,0),
            2
        ),
        0.0
    ) AS average_price
FROM Prices as p
LEFT JOIN UnitsSold as us 
    ON start_date <= purchase_date
    AND purchase_date <= end_date
    AND us.product_id = p.product_id
GROUP BY p.product_id;