from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 6, 14),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG('dbt_dag', default_args=default_args, schedule_interval='0 0 * * *') as dag:
    dbt_task = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run',
        dag=dag
    )