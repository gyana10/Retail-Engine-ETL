{{ config(materialized='table') }}

SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(payment_value) AS lifetime_value,
    AVG(payment_value) AS average_order_value
FROM {{ ref('fact_orders') }}
GROUP BY customer_id