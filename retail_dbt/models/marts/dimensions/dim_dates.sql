{{ config(materialized='table') }}

SELECT DISTINCT
    DATE(order_purchase_timestamp) AS date_key,
    EXTRACT(YEAR FROM order_purchase_timestamp) AS year,
    EXTRACT(MONTH FROM order_purchase_timestamp) AS month,
    EXTRACT(QUARTER FROM order_purchase_timestamp) AS quarter,
    EXTRACT(DAY FROM order_purchase_timestamp) AS day
FROM {{ ref('stg_orders') }}
WHERE order_purchase_timestamp IS NOT NULL