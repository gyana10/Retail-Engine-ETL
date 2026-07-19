"""
### Retail ETL Engine DAG
Orchestrates raw bronze ingestion verification, dbt staging transformations, 
dbt dimensional & fact mart builds, metrics calculations, and data quality testing.
"""

import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_DIR = "/opt/airflow/project/retail_dbt"

default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="retail_etl_pipeline",
    default_args=default_args,
    description="Production Retail ETL pipeline transforming raw Olist data into business metrics",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    max_active_runs=1,
    tags=["retail", "dbt", "postgres", "production"],
) as dag:

    dag.doc_md = __doc__

    start = BashOperator(
        task_id="start_pipeline",
        bash_command="echo 'Retail ETL Pipeline Execution Started'"
    )

    run_staging = BashOperator(
        task_id="run_staging_models",
        bash_command=f"cd {DBT_DIR} && export DBT_PROFILES_DIR={DBT_DIR} && dbt run --select staging"
    )

    run_marts = BashOperator(
        task_id="run_marts_models",
        bash_command=f"cd {DBT_DIR} && export DBT_PROFILES_DIR={DBT_DIR} && dbt run --select marts.dimensions marts.facts"
    )

    run_metrics = BashOperator(
        task_id="run_metrics_models",
        bash_command=f"cd {DBT_DIR} && export DBT_PROFILES_DIR={DBT_DIR} && dbt run --select marts.metrics"
    )

    test_data_quality = BashOperator(
        task_id="test_data_quality",
        bash_command=f"cd {DBT_DIR} && export DBT_PROFILES_DIR={DBT_DIR} && dbt test"
    )

    end = BashOperator(
        task_id="pipeline_complete",
        bash_command="echo 'Retail ETL Pipeline Executed Successfully'"
    )

    start >> run_staging >> run_marts >> run_metrics >> test_data_quality >> end
