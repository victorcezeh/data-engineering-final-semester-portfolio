import os
import json
import logging
import requests
from dotenv import load_dotenv
from google.cloud import storage, bigquery
from google.cloud.exceptions import NotFound, Conflict
from datetime import datetime
from config import PROJECT_ID, BUCKET_NAME, API_URL, SCHEMA_PATH_API, LOCATION

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


def enforce_date_format(date_str: str) -> str:
    """Enforce a specific date format."""
    try:
        # Parse the date and convert it to the desired format
        date_obj = datetime.strptime(date_str, "%b %d, %Y")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        logging.warning(f"Invalid date format: {date_str}")
        return None


def fetch_api_data(api_url: str) -> list:
    """Fetch data from an API and return it as a list of JSON objects."""
    response = requests.get(api_url)
    response.raise_for_status()
    json_data = response.json()
    valid_data = []
    for item in json_data:
        # Assuming 'NorthAmerica' is the date field
        if "NorthAmerica" in item:
            try:
                item["NorthAmerica"] = enforce_date_format(item["NorthAmerica"])
                if item["NorthAmerica"] is not None:
                    valid_data.append(item)
            except ValueError:
                logging.warning(
                    f"Invalid date format for 'NorthAmerica' field: {item['NorthAmerica']}"
                )
    return valid_data


def upload_to_gcs(bucket_name: str, blob_name: str, data: str) -> None:
    """Upload data to a Google Cloud Storage bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    if not client.lookup_bucket(bucket_name):
        bucket = client.create_bucket(
            bucket_name, location=LOCATION, storage_class="STANDARD"
        )
        logging.info(f"Bucket '{bucket_name}' created successfully.")
    else:
        logging.info(f"Bucket '{bucket_name}' already exists.")

    blob = bucket.blob(blob_name)
    blob.upload_from_string(data, content_type="application/json")
    logging.info(f"Data uploaded to blob '{blob_name}' successfully.")


def create_bigquery_dataset(client: bigquery.Client, dataset_id: str) -> None:
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


def create_bigquery_table(
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

        # Modify the schema to enforce date format for date fields
        for field in schema:
            if field["type"] == "DATE":
                field["mode"] = "NULLABLE"  # Optionally, adjust the mode as needed

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


def load_data_from_gcs_to_bq(
    client: bigquery.Client,
    gcs_uri: str,
    dataset_id: str,
    table_id: str,
    schema_path: str,
) -> None:
    """Load data from a Google Cloud Storage bucket into a BigQuery table."""
    try:
        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)

        table_ref = f"{client.project}.{dataset_id}.{table_id}"
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            schema=[bigquery.SchemaField.from_api_repr(field) for field in schema],
        )

        load_job = client.load_table_from_uri(gcs_uri, table_ref, job_config=job_config)
        load_job.result()
        logging.info(
            f"Data loaded into BigQuery table '{dataset_id}.{table_id}' successfully."
        )
    except Exception as e:
        logging.error(
            f"Error loading data from GCS to BigQuery table '{dataset_id}.{table_id}': {e}"
        )
        raise e


if __name__ == "__main__":
    client = bigquery.Client(project=PROJECT_ID)

    # Fetch API data and upload to GCS
    json_data = fetch_api_data(API_URL)
    json_lines = "\n".join([json.dumps(item) for item in json_data])
    blob_name = "playstation_games_api.jsonl"
    upload_to_gcs(BUCKET_NAME, blob_name, json_lines)

    # Create dataset and table in BigQuery
    dataset_id = "gcs_load_bq"
    table_id = "playstation_games_api"
    create_bigquery_dataset(client, dataset_id)
    create_bigquery_table(client, PROJECT_ID, dataset_id, table_id, SCHEMA_PATH_API)

    # Load data from GCS to BigQuery
    gcs_uri = f"gs://{BUCKET_NAME}/{blob_name}"
    load_data_from_gcs_to_bq(client, gcs_uri, dataset_id, table_id, SCHEMA_PATH_API)
