# deploy/airflow/dags/ml_pipeline_dag.py
from __future__ import annotations
import json
import sys
from datetime import datetime
from pathlib import Path

# so "from src import ..." works inside Airflow containers
sys.path.insert(0, "/opt/airflow")

from airflow import DAG
from airflow.operators.python import PythonOperator

# Mounted, shared paths
OUTPUT_DIR = Path("/opt/airflow/outputs")
DATA_DIR = OUTPUT_DIR / "data"
MODELS_DIR = OUTPUT_DIR / "models"
SRC_DIR = Path("/opt/airflow/src")  # where salaries.csv lives in your image
MODEL_PATH = MODELS_DIR / "model.pkl"
METRICS_PATH = MODELS_DIR / "metrics.json"

for p in (DATA_DIR, MODELS_DIR):
    p.mkdir(parents=True, exist_ok=True)


def t_preprocess(**_):
    from src.data_preprocessing import (
        load_data,
        filter_data_scientist,
        preprocess_and_split,
    )
    import joblib

    df = load_data(SRC_DIR / "salaries.csv")
    df = filter_data_scientist(df)
    X_train, X_test, y_train, y_test = preprocess_and_split(df)
    joblib.dump((X_train, y_train), DATA_DIR / "train.pkl")
    joblib.dump((X_test, y_test), DATA_DIR / "test.pkl")
    print("Preprocess saved:", (DATA_DIR / "train.pkl"), (DATA_DIR / "test.pkl"))


def t_feature_engineering(**_):
    import joblib
    import pandas as pd
    from src.feature_engineering import (
        create_feature_transformer,
        fit_transform_features,
        transform_features,
    )

    # load splits saved by preprocess step
    X_train, y_train = joblib.load(DATA_DIR / "train.pkl")
    X_test, y_test = joblib.load(DATA_DIR / "test.pkl")

    # ensure DataFrame (ColumnTransformer relies on column names)
    if not hasattr(X_train, "columns"):
        X_train = pd.DataFrame(X_train)
    if not hasattr(X_test, "columns"):
        X_test = pd.DataFrame(X_test)

    # build + fit on train, transform both
    pre = create_feature_transformer(X_train)
    X_train_fe = fit_transform_features(pre, X_train)
    X_test_fe = transform_features(pre, X_test)

    # persist engineered splits and the preprocessor
    joblib.dump((X_train_fe, y_train), DATA_DIR / "train_fe.pkl")
    joblib.dump((X_test_fe, y_test), DATA_DIR / "test_fe.pkl")
    joblib.dump(pre, MODELS_DIR / "preprocessor.pkl")
    print(
        "Feature engineering saved:",
        DATA_DIR / "train_fe.pkl",
        DATA_DIR / "test_fe.pkl",
        MODELS_DIR / "preprocessor.pkl",
    )


def t_train(**_):
    from src.training import train_model
    import joblib

    X_train_fe, y_train = joblib.load(DATA_DIR / "train_fe.pkl")
    model, results = train_model(
        X_train_fe, y_train, n_jobs=-1, output_dir=str(OUTPUT_DIR)
    )
    joblib.dump(model, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(results, indent=2))
    print("Model saved:", MODEL_PATH)
    print("Training metrics saved:", METRICS_PATH)


def t_evaluate(**_):
    from src.evaluation import evaluate
    import joblib

    X_test_fe, y_test = joblib.load(DATA_DIR / "test_fe.pkl")
    model = joblib.load(MODEL_PATH)
    eval_metrics = evaluate(model, X_test_fe, y_test)
    try:
        all_metrics = json.loads(METRICS_PATH.read_text())
    except FileNotFoundError:
        all_metrics = {}
    all_metrics["evaluation"] = eval_metrics
    METRICS_PATH.write_text(json.dumps(all_metrics, indent=2))
    print("Evaluation metrics appended:", METRICS_PATH)


with DAG(
    dag_id="ml_pipeline_dag",
    description="Preprocess → FeatureEng → Train → Evaluate",
    start_date=datetime(2025, 8, 1),
    schedule="@weekly",
    catchup=False,
    default_args={"owner": "airflow", "retries": 0},
    tags=["ml"],
):
    preprocess = PythonOperator(task_id="preprocess", python_callable=t_preprocess)
    feature_eng = PythonOperator(
        task_id="feature_engineering", python_callable=t_feature_engineering
    )
    train = PythonOperator(task_id="train", python_callable=t_train)
    evaluate = PythonOperator(task_id="evaluate", python_callable=t_evaluate)

    preprocess >> feature_eng >> train >> evaluate
