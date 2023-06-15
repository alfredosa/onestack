from pendulum import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from cosmos.providers.dbt.task_group import DbtTaskGroup


with DAG(
    dag_id="extract_dag",
    start_date=datetime(2022, 11, 27),
    schedule="@daily",
):
    e1 = EmptyOperator(task_id="pre_dbt")

    dbt_tg = DbtTaskGroup(
        dbt_project_name="onestack",
        conn_id="postgres",
        profile_args={
            "schema": "public",
        },
    )

    e2 = EmptyOperator(task_id="post_dbt")

    e1 >> dbt_tg >> e2
