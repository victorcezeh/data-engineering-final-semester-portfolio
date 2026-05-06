import os
import json
import logging
from dotenv import load_dotenv
from google.cloud import bigquery
from google.cloud.exceptions import NotFound, Conflict
from config import PROJECT_ID, DATASET_ID, TABLE_ID, FILE_PATH, SCHEMA_PATH_CSV

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


def create_dataset(client: bigquery.Client, dataset_id: str) -> None:
    """Create a BigQuery dataset if it does not exist."""
    try:
        dataset_ref = client.dataset(dataset_id)
        client.create_dataset(dataset_ref)
        logging.info(f"Dataset {dataset_id} created successfully!")
    except Conflict:
        logging.info(f"Dataset {dataset_id} already exists.")
    except Exception as e:
        logging.error(f"Error creating dataset {dataset_id}: {e}")
        raise e


def create_table(
    client: bigquery.Client,
    project_id: str,
    dataset_id: str,
    table_id: str,
    schema_path: str,
) -> None:
    """Create a BigQuery table with the provided schema if it does not exist."""
    try:
        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)

        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        table = bigquery.Table(
            table_ref,
            schema=[bigquery.SchemaField.from_api_repr(field) for field in schema],
        )
        client.create_table(table)
        logging.info(f"Table {table_id} created successfully in dataset {dataset_id}.")
    except Conflict:
        logging.info(f"Table {table_id} already exists in dataset {dataset_id}.")
    except Exception as e:
        logging.error(f"Error creating table {table_id}: {e}")
        raise e


def insert_csv_into_table(
    client: bigquery.Client, table_ref: str, file_path: str, schema_path: str
) -> None:
    """Insert data from a CSV file into the specified BigQuery table."""
    try:
        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)

        job_config = bigquery.LoadJobConfig(
            schema=[bigquery.SchemaField.from_api_repr(field) for field in schema],
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
        )

        with open(file_path, "rb") as source_file:
            load_job = client.load_table_from_file(
                source_file, table_ref, job_config=job_config
            )
        load_job.result()
        logging.info(f"CSV file successfully loaded into table {table_ref}!")
    except Exception as e:
        logging.error(f"Error loading CSV file into table {table_ref}: {e}")
        raise e


if __name__ == "__main__":
    client = bigquery.Client(project=PROJECT_ID)

    # Create dataset and table
    create_dataset(client, DATASET_ID)
    create_table(client, PROJECT_ID, DATASET_ID, TABLE_ID, SCHEMA_PATH_CSV)

    # Load CSV data into table
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    insert_csv_into_table(client, table_ref, FILE_PATH, SCHEMA_PATH_CSV)
