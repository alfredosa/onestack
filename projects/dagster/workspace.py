from dagster import repository
from download import download_yahoo_finance_files


@repository
def workspace():
    return [
        download_yahoo_finance_files
    ]
