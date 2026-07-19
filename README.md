# 🚀 Production Retail ETL Engine & Analytical Data Warehouse

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)]()
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.10-red.svg)]()
[![dbt](https://img.shields.io/badge/dbt-Data%20Build%20Tool-orange.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

A **production-grade Data Engineering pipeline** that ingests raw e-commerce data, transforms it using the **Medallion Architecture (Bronze → Silver → Gold)**, builds a **Kimball Star Schema**, validates data quality with **dbt tests**, and orchestrates the complete workflow using **Apache Airflow** inside a fully containerized Docker environment.

---

# 📌 Project Overview

This project demonstrates an end-to-end modern Data Engineering workflow using the **Olist Brazilian E-Commerce Dataset (100K+ records)**.

The pipeline automates:

- Raw data ingestion into PostgreSQL
- Data cleansing & standardization
- Dimensional modeling (Kimball Star Schema)
- Business KPI generation
- Automated data quality validation
- Workflow orchestration with Airflow
- Fully reproducible Docker deployment

---

# 🏗 Architecture

```
                     +-------------------------+
                     |     Raw CSV Files       |
                     |  (Olist E-Commerce)     |
                     +-----------+-------------+
                                 |
                                 |
                                 ▼
                   Python + SQLAlchemy Loader
                                 |
                                 ▼
                 Bronze Layer (PostgreSQL Tables)
                                 |
                                 |
                          dbt Staging Models
                                 |
                                 ▼
                 Silver Layer (Cleaned Views)
                                 |
                                 |
                    dbt Mart Transformations
                                 |
                                 ▼
          Gold Layer (Fact & Dimension Tables)
                                 |
                                 |
                    dbt Metric Aggregations
                                 |
                                 ▼
             Executive Business Metrics (KPIs)
                                 |
                                 |
                         dbt Data Quality Tests
                                 |
                                 ▼
                  Apache Airflow DAG Orchestration
```

---

# 🏛 Medallion Architecture

## 🥉 Bronze Layer
Raw ingestion from CSV files into PostgreSQL without business transformations.

Tables include:

- Customers
- Orders
- Order Items
- Payments
- Products
- Sellers
- Category Translation

---

## 🥈 Silver Layer

dbt staging models perform:

- Data type casting
- Null handling
- String normalization
- Column standardization
- Data cleaning

---

## 🥇 Gold Layer

Business-ready analytical warehouse using Kimball dimensional modeling.

### Fact Table

- fact_orders

### Dimension Tables

- dim_customers
- dim_products
- dim_sellers
- dim_dates

---

# 📊 Business Metrics

The pipeline generates:

- Monthly Revenue
- Customer Lifetime Value (LTV)
- Top Customers
- Repeat Purchase Rate

These tables are immediately consumable by BI tools such as Power BI or Tableau.

---

# ✅ Data Quality

The pipeline automatically validates data using **dbt tests** before completion.

Checks include:

- Unique primary keys
- NOT NULL constraints
- Source validation
- Schema integrity

If validation fails, the Airflow pipeline stops automatically.

---

# ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Orchestration | Apache Airflow 2.10 |
| Transformations | dbt |
| Database | PostgreSQL 15 |
| Programming | Python |
| Data Processing | Pandas |
| ORM | SQLAlchemy |
| Containerization | Docker & Docker Compose |
| Modeling | Kimball Star Schema |
| Architecture | Medallion Architecture |
| Version Control | Git |

---

# 📁 Project Structure

```
Retail_ETL_Engine/
│
├── airflow/
│   └── dags/
│       └── retail_pipeline.py
│
├── retail_dbt/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   │       ├── dimensions/
│   │       ├── facts/
│   │       └── metrics/
│   │
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── scripts/
│   └── load_raw_data.py
│
├── sql/
│   └── create_bronze_tables.sql
│
├── data/
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🚀 Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/gyana10/Retail-Engine-ETL.git

cd Retail-Engine-ETL
```

### 2. Start Docker

```bash
docker compose up -d --build
```

### 3. Load Bronze Data

```bash
docker exec -it airflow_scheduler \
python /opt/airflow/project/scripts/load_raw_data.py
```

### 4. Open Airflow

```
http://localhost:8080
```

Username

```
admin
```

Password

```
admin
```

### 5. Trigger Pipeline

```bash
docker exec -it airflow_scheduler \
airflow dags trigger retail_etl_pipeline
```

---

# 📈 Pipeline Flow

```
CSV Files
    │
    ▼
Python Loader
    │
    ▼
Bronze Tables
    │
    ▼
dbt Staging
    │
    ▼
dbt Marts
    │
    ▼
Business Metrics
    │
    ▼
dbt Tests
    │
    ▼
Airflow Success
```

---

# 🎯 Key Features

- End-to-End ETL Pipeline
- Medallion Architecture
- Kimball Star Schema
- Apache Airflow Orchestration
- dbt Modular Transformations
- Automated Data Quality Testing
- Dockerized Infrastructure
- PostgreSQL Data Warehouse
- Idempotent Pipeline Design
- Production-ready Repository Structure

---

# 📚 Skills Demonstrated

- Data Engineering
- ETL Development
- Workflow Orchestration
- Data Warehouse Design
- Dimensional Modeling
- SQL Optimization
- Docker Containerization
- PostgreSQL
- Python Automation
- Data Quality Engineering
- Git & Version Control

---

# 👨‍💻 Author

**Gyana Ranjan Mohanty**

B.Tech Computer Science (Data Science)

Passionate about Data Engineering, Machine Learning, and Cloud Technologies.

GitHub:
https://github.com/gyana10