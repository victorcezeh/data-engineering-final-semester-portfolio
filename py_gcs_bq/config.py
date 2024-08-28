import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project Constants
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
DATASET_ID = "etl_basics"
TABLE_ID = "klitch_sales_dataset"
FILE_PATH = "C:/Users/Victor/Desktop/Final_Semester/data-engineering-final-semester-portfolio/py_gcs_bq/data/klitch_sales_dataset.csv"
SCHEMA_PATH_CSV = "C:/Users/Victor/Desktop/Final_Semester/data-engineering-final-semester-portfolio/py_gcs_bq/schemas/klitch_sales_dataset_schema.json"
API_URL = "https://api.sampleapis.com/playstation/games"
SCHEMA_PATH_API = "C:/Users/Victor/Desktop/Final_Semester/data-engineering-final-semester-portfolio/py_gcs_bq/schemas/api_schema.json"
LOCATION = "europe-west1"

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv(
    "GOOGLE_APPLICATION_CREDENTIALS"
)
