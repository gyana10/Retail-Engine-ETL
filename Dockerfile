FROM apache/airflow:2.10.2

USER airflow

RUN pip install --no-cache-dir dbt-postgres pandas sqlalchemy psycopg2-binary