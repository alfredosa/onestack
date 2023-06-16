from dagster import job, repository
from dagster_pyspark import pyspark_resource

from db import initialize_db, drop_tables_op, create_schemas_op, trino_resource
from download import download_all_files
from dbt_pipeline import dbt_all
from predict import predict_op



@repository
def workspace():
    return [
        initialize_db,
        download_all_files,
        dbt_all,
    ]
