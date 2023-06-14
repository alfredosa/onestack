FROM apache/airflow:latest-python3.10

USER root

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install poetry --no-user

WORKDIR /opt/airflow

COPY poetry.lock pyproject.toml ./

RUN python3 -m venv /opt/airflow/.venv
RUN /opt/airflow/.venv/bin/pip install --no-cache-dir poetry --no-user
RUN /opt/airflow/.venv/bin/poetry install --no-interaction --no-ansi

COPY ./airflow/dags/ /opt/airflow/dags/

COPY ./airflow/airflow.cfg /opt/airflow/airflow.cfg

RUN chown -R airflow: /opt/airflow

USER airflow

