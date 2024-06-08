![this-is-the-cloud](https://github.com/victorcezeh/data-engineering-final-semester-portfolio/assets/129629266/38d4437e-e9b8-4479-92aa-7695047db583)



# Google Cloud Storage (GCS) and BigQuery (BQ) Data Pipeline

This repository contains scripts to set up a data pipeline for loading data from various sources into Google Cloud Storage (GCS) and then into BigQuery (BQ). The pipeline fetches data from an API, transforms it if necessary, uploads it to GCS as JSON Lines files, and loads CSV files directly into BigQuery.

## Table of Contents
1. [File Structure](#file-structure)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Idempotency](#idempotency)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

## File Structure

```
├── README.md
├── load_api_to_gcs_bq.py
├── load_csv_to_bq.py
├── config.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── LICENSE
└── schema
    ├── api_schema.json
    └── csv_schema.json
```

- `load_api_to_gcs_bq.py`: Main script to fetch data from API, upload to GCS, and load into BQ.
- `load_csv_to_bq.py`: Script to load CSV files directly into BigQuery tables.
- `config.py`: Configuration file to manage project constants.
- `.env`: File to store environment variables (not included in version control).
- `.env.example`: Example template for environment variables. Rename to `.env` and fill in your credentials.
- `.gitignore`: File to specify which files and directories to ignore in version control.
- `requirements.txt`: List of dependencies required by the project.
- `LICENSE`: File containing the license under which the project is distributed.
- `schema/`: Directory containing JSON schema files for BQ tables.

## Features

- **Fetch API Data**: Fetch data from an API endpoint and transform it if necessary.
- **Upload to GCS**: Upload data to Google Cloud Storage as JSON Lines files for further processing.
- **Load CSV to BQ**: Load CSV files directly into BigQuery tables without intermediate storage.
- **Dynamic Dataset and Table Creation**: Create BigQuery datasets and tables dynamically if they don't already exist.
- **Idempotency and Data Integrity**: Ensure that data loading processes are idempotent and maintain data integrity.
- **Date Formatting**: Handle date formatting to ensure consistency in the data.
- **Reusable and Extensible Code Structure**: Follow DRY principles for maintainability.
- **Secrets Management**: Manage secrets and sensitive information using `.env` files.

## Prerequisites

Before running the scripts, ensure you have the following:

1. **Google Cloud Platform (GCP) Account**: Access to GCP to use GCS and BQ services.
2. **Service Account Key**: Generate a service account key with appropriate permissions for GCS and BQ.
3. **Python Environment**: Python 3.7+ environment with necessary dependencies installed. You can install dependencies using `pip install -r requirements.txt`.
4. **Configuration Files**: Create a `.env` file with necessary credentials and a `config.py` file to manage project constants. Use `.env.example` as a template.

## Installation

To use the scripts, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/victorcezeh/py_gcs_bq.git
    cd py_gcs_bq
    ```

2. **Set Up Configuration Files**:

    - Copy `.env.example` to `.env` and fill in your GCP credentials and other environment variables.
    - Modify `config.py` to manage project constants such as project ID, dataset ID, etc.

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place your CSV file** in the `data/` directory.
2. **Update the `config.py` file** with your project constants.
3. **Run the ETL process**:

    ```bash
    python load_csv_to_bq.py
    ```

    This will:
    - Create a `etl_basics` dataset in BigQuery (if it doesn't exist).
    - Load your CSV file into a BigQuery table using the schema from `schema/klitch_sales_dataset_schema.json`.

4. **Fetch and Load API Data**:

    ```bash
    python load_api_to_gcs_bq.py
    ```

    This will:
    - Fetch data from the specified API.
    - Store the data in a GCS bucket as JSONL.
    - Load the JSONL data into a BigQuery table using the schema from `schema/api_schema.json`.

## Configuration

- `config.py`: Contains project constants like dataset names, table names, and GCS bucket names.
- `.env`: Contains sensitive information like API keys, GCP project ID, and service account details.
- `.env.example`: A template for `.env`, showing required environment variables without values.

## Idempotency

The code is designed to be idempotent, ensuring that running it multiple times with the same data will not result in duplicate records in BigQuery. This is achieved by:

- Checking if datasets and tables exist before attempting to create them, preventing duplication of resources.
- Employing proper data loading techniques that ensure existing data is overwritten or appended to as necessary, depending on the data loading requirements. This is achieved without causing duplication or data inconsistencies.

## Contributing

Contributions are welcome! Please feel free to open issues for any bugs, feature requests, or suggestions. Pull requests are also appreciated.

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgements

I am deeply grateful to [Altschool Africa](https://altschoolafrica.com/) and [JesuFemi-O](https://github.com/JesuFemi-O) for equipping me with the expertise required to successfully undertake this project.
