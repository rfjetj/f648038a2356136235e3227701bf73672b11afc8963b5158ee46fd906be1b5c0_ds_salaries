# Airflow 2.9.x with Python 3.12
FROM apache/airflow:2.9.3-python3.12

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

ARG AIRFLOW_VERSION=2.9.3
ARG PYTHON_VERSION=3.12
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Install ONLY what DAGs/operators need (respect Airflow constraints!)
COPY deploy/airflow/requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Bake your project code (src + salaries.csv) into the image
# (this path is relative to the REPO ROOT build context)
COPY src /opt/airflow/src