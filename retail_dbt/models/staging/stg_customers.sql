{{ config(
    materialized='view'
) }}

SELECT
    customer_id,
    customer_unique_id,
    INITCAP(customer_city) AS customer_city,
    UPPER(customer_state) AS customer_state
FROM {{ source('bronze', 'customers') }}