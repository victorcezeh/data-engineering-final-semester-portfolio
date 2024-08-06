from datetime import timedelta
import os
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

ENV = os.environ.get("ENV", "dev")
DEFAULT_ARGS = {
    "owner": "Victor Ezeh",
    "retries": 2,
    "retry_delay": timedelta(minutes=3),
    "start_date": "2024-07-17",
    
    
}

with DAG(
    dag_id=f"{ENV}-astronauts_in_space-v1.0",
    description="Get astronauts in space",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    max_active_runs=1,
    catchup=False,
    tags=["dbt"],
) as dag:
    start=EmptyOperator(task_id='start')
    end=EmptyOperator(task_id='end')
    run_endpoint1=SimpleHttpOperator(
        task_id="run-endpoint1",
        endpoint="astros.json",
        method="GET",
        log_response=True,
    )
    run_endpoint2 = SimpleHttpOperator(
        task_id="run-endpoint2",
        endpoint="iss-now.json",
        method="GET",
        log_response=True,
    )
    
    start >> [run_endpoint1, run_endpoint2] >> end