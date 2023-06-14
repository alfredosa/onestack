FROM apache/airflow:latest

USER root

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set up the working directory
WORKDIR /opt/airflow

# Copy the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy your DAGs into the container
COPY ./airflow/dags/ /opt/airflow/dags/

# Copy your Airflow configuration file into the container
COPY ./airflow/airflow.cfg /opt/airflow/airflow.cfg

# Set the ownership and permissions for the copied files
RUN chown -R airflow: /opt/airflow

USER airflow

