{{ config(materialized='table') }}

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(DISTINCT order_id) AS orders_count
    FROM {{ ref('fact_orders') }}
    GROUP BY customer_id
)

SELECT
    COUNT(CASE WHEN orders_count > 1 THEN 1 END)::FLOAT
    / COUNT(*) * 100 AS repeat_purchase_rate
FROM customer_orders