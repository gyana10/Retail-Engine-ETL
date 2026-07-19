{{ config(materialized='table') }}

SELECT
    DATE_TRUNC('month', order_date) AS revenue_month,
    SUM(payment_value) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM {{ ref('fact_orders') }}
GROUP BY 1
ORDER BY 1