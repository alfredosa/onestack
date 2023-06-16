from dagster import repository

from db import initialize_db
from download import download_all_files
from dbt_pipeline import dbt_all



@repository
def workspace():
    return [
        initialize_db,
        download_all_files,
        dbt_all,
    ]
