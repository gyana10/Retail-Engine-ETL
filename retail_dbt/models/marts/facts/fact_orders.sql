{{ config(materialized='table') }}

SELECT
    oi.order_id,
    o.customer_id,
    oi.product_id,
    oi.seller_id,
    DATE(o.order_purchase_timestamp) AS order_date,

    oi.price,
    oi.freight_value,

    p.payment_type,
    p.payment_installments,
    p.payment_value

FROM {{ ref('stg_order_items') }} oi
JOIN {{ ref('stg_orders') }} o
    ON oi.order_id = o.order_id
LEFT JOIN {{ ref('stg_payments') }} p
    ON oi.order_id = p.order_id