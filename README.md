# Retail ETL Engine (Production Data Engineering Pipeline)

A production-grade, containerized Retail Data Pipeline built with **Apache Airflow**, **dbt (data build tool)**, **PostgreSQL**, **Python**, and **Docker Compose**, processing the **Olist Brazilian E-Commerce Dataset**.

---

## 🏗️ Architecture & Data Layer Flow

```
+-----------------------------------------------------------------------------------+
|                                RAW LAYER (CSV Data)                               |
| (customers, orders, order_items, payments, products, sellers, category_trans)   |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼ [scripts/load_raw_data.py]
+-----------------------------------------------------------------------------------+
|                             BRONZE SCHEMA (PostgreSQL)                            |
| Raw tabular ingestion with strict schema DDL & idempotent truncation             |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼ [dbt run --select staging]
+-----------------------------------------------------------------------------------+
|                             STAGING LAYER (dbt Views)                             |
| Type casting, column renaming, null handling, string normalization                |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼ [dbt run --select marts.dimensions marts.facts]
+-----------------------------------------------------------------------------------+
|                        MARTS LAYER (Star Schema Tables)                           |
| Fact: fact_orders | Dimensions: dim_customers, dim_products, dim_sellers, dim_dates |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼ [dbt run --select marts.metrics]
+-----------------------------------------------------------------------------------+
|                             BUSINESS METRICS LAYER                                |
| Executive tables: customer_ltv, monthly_revenue, repeat_purchase_rate, top_cust   |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼ [dbt test]
+-----------------------------------------------------------------------------------+
|                           DATA QUALITY & TESTING GATE                             |
| Uniqueness, Non-nullability, Schema validation assertions                        |
+-----------------------------------------------------------------------------------+
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Docker & Docker Compose
- Python 3.9+ (optional for local raw data loader execution)

### 1. Spin up Container Infrastructure
```bash
docker-compose up -d --build
```

### 2. Ingest Raw Bronze Layer
```bash
docker exec -it airflow_scheduler python /opt/airflow/project/scripts/load_raw_data.py
```

### 3. Access Airflow Web Interface
- **URL**: `http://localhost:8080`
- **Username**: `admin`
- **Password**: `admin`

### 4. Trigger Pipeline Execution
- Enable and trigger `retail_etl_pipeline` from the Airflow Web UI or run:
```bash
docker exec -it airflow_scheduler airflow dags trigger retail_etl_pipeline
```

---

## 📁 Repository Structure

```
Retail_ETL_Engine/
├── Dockerfile                  # Airflow container build with dbt & database dependencies
├── docker-compose.yml          # Multi-container orchestration (Postgres, Scheduler, Webserver)
├── README.md                   # Project documentation
├── airflow/
│   └── dags/
│       └── retail_pipeline.py  # Production Airflow DAG orchestrating ETL workflow
├── data/                       # Raw Olist E-commerce CSV datasets
├── retail_dbt/                 # dbt project root
│   ├── dbt_project.yml         # dbt project configuration
│   ├── profiles.yml            # PostgreSQL connection profiles
│   └── models/
│       ├── staging/            # Bronze -> Silver views and schema tests
│       └── marts/              # Silver -> Gold star schema tables and metric models
├── scripts/
│   └── load_raw_data.py        # Python automated ingestion script to Bronze schema
└── sql/
    └── create_bronze_tables.sql# DDL statements for Bronze tables
```

---

## 🛠️ Technology Stack & Key Decisions

- **Orchestrator**: Apache Airflow 2.10 (LocalExecutor, PostgreSQL metadata backend).
- **Transformation Engine**: dbt (data build tool) with `dbt-postgres` adapter.
- **Database**: PostgreSQL 15.
- **Containerization**: Docker Compose for isolated microservices and reproducible execution environment.
