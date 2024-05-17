![Docker](https://github.com/victorcezeh/data-engineering-final-semester-portfolio/assets/129629266/3fb3c509-32e3-4b50-a273-ee9d049f45bd)


# Postgres Docker Setup

This project sets up a basic Postgres infrastructure using Docker and Docker Compose. The goal is to facilitate the setup, loading of data, and interaction with Postgres from Python.

## Table of Contents

- [Project Structure](#project-structure)
- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
  - [macOS](#macos)
  - [Windows](#windows)
- [Usage](#usage)
- [Contributing](#contributing)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Acknowledgements](#acknowledgements)

## Project Structure

```
postgres_docker_init/
│
├── README.md
│
├── data/
│   └── customer.csv
│
├── infrastructure_scripts/
│   └── init.sql
│
└── src/
    ├── db_manager.py
    └── main.py
```

- **README.md**: Documentation for the project.
- **data/**: Contains the `customer.csv` data file.
- **infrastructure_scripts/**: Includes the SQL initialization script `init.sql`.
- **src/**: Contains Python scripts:
  - `db_manager.py`: Connects to the Postgres database.
  - `main.py`: Entry point for executing queries and interacting with the database.

## Project Description


In this project, I demonstrated my ability to set up a Postgres server leveraging Docker and Docker Compose. The objective was to test my skills in setting up, loading data, and interacting with Postgres from Python.


### Features

- Setup a Postgres database using Docker.
- Load data from a CSV file into the database.
- Interact with the database using Python scripts.

## Setup Instructions

### macOS

1. **Clone Repository**:
   ```bash
   git clone <repository_url>
   cd postgres_docker_init
   ```

2. **Start Docker**:
   - Ensure Docker is installed and running.

3. **Run Docker Compose**:
   ```bash
   docker-compose up
   ```

4. **Execute Python Scripts**:
   - Open a terminal window.
   - Navigate to the project directory.
   - Run the Python scripts:
     ```bash
     python src/main.py
     ```

### Windows

1. **Clone Repository**:
   ```bash
   git clone <repository_url>
   cd postgres_docker_init
   ```

2. **Start Docker**:
   - Ensure Docker is installed and running.

3. **Run Docker Compose**:
   ```bash
   docker-compose up
   ```

4. **Execute Python Scripts**:
   - Open a command prompt.
   - Navigate to the project directory.
   - Run the Python scripts:
     ```bash
     python src/main.py
     ```

## Usage

1. **Start Postgres Server**:
   - Use Docker Compose to start the Postgres server:
     ```bash
     docker-compose up
     ```

2. **Load Data**:
   - The `init.sql` script will automatically create the schema, table, and load data from `customer.csv` into the database.

3. **Run Python Scripts**:
   - Use the `main.py` script to connect to the Postgres database and execute a query:
     ```bash
     python src/main.py
     ```

## Contributing

1. **Create a New Branch**:
   - Create a new local branch with a name of your choice:
     ```bash
     git checkout -b <branch_name>
     ```

2. **Commit and Push**:
   - Commit your changes and push them to your remote repository:
     ```bash
     git add .
     git commit -m "Your commit message"
     git push origin <branch_name>
     ```

3. **Pull Request**:
   - Open a pull request and request a review.
   - Provide a brief summary of the changes made.

## Environment Variables

Make sure to set up the following environment variables in a `.env` file at the root of your project:

```
POSTGRES_USER=ink_store_user
POSTGRES_PASSWORD=thelaw0000
POSTGRES_DB=ink_store_db
POSTGRES_PORT=5434
POSTGRES_HOST=localhost
```

This configuration will be used by the `db_manager.py` script to connect to the Postgres database.

## Troubleshooting

- **Docker Compose Issues**:
  - Ensure Docker is running and properly installed.
  - Verify that the Docker Compose file is correctly formatted.
  - Check for any port conflicts and adjust the `docker-compose.yml` file as needed.

- **Database Connection Problems**:
  - Ensure that the environment variables are correctly set up.
  - Confirm that the Postgres container is running and accessible.
  - Check network settings and firewall configurations.

- **Python Script Errors**:
  - Ensure all required Python packages are installed:
    ```bash
    pip install -r requirements.txt
    ```
  - Verify the database connection settings in `db_manager.py`.

## Acknowledgements

I wish to express my sincere appreciation to [Altschool Africa](https://altschoolafrica.com/) and [jesufemi-o](https://github.com/JesuFemi-O) for empowering me with the expertise essential for executing this project.
