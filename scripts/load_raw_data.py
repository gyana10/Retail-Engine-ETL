import os
import logging
import pandas as pd
from sqlalchemy import create_engine, text

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Database configuration from environment variables with production defaults
DB_USER = os.getenv("POSTGRES_USER", "airflow")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "airflow")
DB_HOST = os.getenv("POSTGRES_HOST", "postgres-airflow")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "airflow")

# Derive project root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SQL_FILE = os.path.join(BASE_DIR, "sql", "create_bronze_tables.sql")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}

def load_bronze_layer():
    logger.info(f"Connecting to database at {DB_HOST}:{DB_PORT}/{DB_NAME}...")
    engine = create_engine(DATABASE_URL)

    # Step 1: Ensure bronze schema and tables exist
    if os.path.exists(SQL_FILE):
        logger.info("Executing DDL to ensure bronze schema and tables exist...")
        with open(SQL_FILE, "r") as f:
            ddl_sql = f.read()
        with engine.begin() as conn:
            for statement in ddl_sql.split(";"):
                stmt = statement.strip()
                if stmt:
                    conn.execute(text(stmt))
        logger.info("Bronze schema DDL executed successfully.")

    # Step 2: Load CSV files into bronze schema
    for table_name, file_name in files.items():
        file_path = os.path.join(DATA_DIR, file_name)
        if not os.path.exists(file_path):
            logger.warning(f"File {file_path} not found. Skipping {table_name}.")
            continue

        logger.info(f"Loading {table_name} from {file_name}...")
        df = pd.read_csv(file_path)

        # Truncate existing data to allow clean re-runs (idempotent loading)
        with engine.begin() as conn:
            conn.execute(text(f"TRUNCATE TABLE bronze.{table_name} CASCADE;"))

        df.to_sql(
            table_name,
            engine,
            schema="bronze",
            if_exists="append",
            index=False,
            method="multi",
            chunksize=10000
        )
        logger.info(f"Table bronze.{table_name} loaded successfully ({len(df)} records).")

    logger.info("Bronze layer ingestion completed successfully.")

if __name__ == "__main__":
    load_bronze_layer()