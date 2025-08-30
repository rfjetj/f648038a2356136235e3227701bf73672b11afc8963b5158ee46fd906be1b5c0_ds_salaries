FROM apache/airflow:2.10.3

USER airflow

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY --chown=airflow:0 pyproject.toml uv.lock* ./

RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install -r requirements.txt

RUN mkdir -p /app/data /app/data/raw /app/data/preprocessed /app/models /app/reports /app/logs && \
    chown -R airflow:0 /app/data /app/data/raw /app/data/preprocessed /app/models /app/reports /app/logs
