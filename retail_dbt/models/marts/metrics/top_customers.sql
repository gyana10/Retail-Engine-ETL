{{ config(materialized='table') }}

SELECT
    customer_id,
    SUM(COALESCE(payment_value,0)) AS total_spent,
    COUNT(DISTINCT order_id) AS total_orders
FROM {{ ref('fact_orders') }}
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10