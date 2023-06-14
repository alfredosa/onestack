FROM apache/airflow:latest-python3.10

USER root

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install poetry --no-user

WORKDIR /opt/airflow

COPY poetry.lock pyproject.toml ./

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    default-libmysqlclient-dev \
    libpq-dev \
    freetds-bin \
    freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry dependencies
RUN python3 -m venv /opt/airflow/.venv
RUN /opt/airflow/.venv/bin/pip install --no-cache-dir poetry --no-user
RUN /opt/airflow/.venv/bin/poetry install --no-interaction --no-ansi

COPY ./airflow/dags/ /opt/airflow/dags/

COPY ./airflow/airflow.cfg /opt/airflow/airflow.cfg

COPY ./.env /opt/airflow/.env

RUN chown -R airflow: /opt/airflow

USER airflow

ENTRYPOINT ["bash", "-c", "source /opt/airflow/.env && airflow db init && airflow users create --username onestack --firstname One --lastname Stack --role Admin --email onestack@example.com --password onestack && airflow webserver"]
