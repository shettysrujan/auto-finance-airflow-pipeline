# loan_risk_pipeline.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# DAG definition
dag = DAG(
    dag_id='auto_finance_risk_pipeline',
    description='Pipeline to calculate loan risk using Spark',
    schedule_interval=None,  # manual trigger or cron string
    start_date=datetime(2026, 3, 1),
    catchup=False,
    tags=['finance', 'spark'],
)

# Environment variables
SPARK_HOME = "/home/ec2-user/spark"
SPARK_JOB_PATH = "/home/ec2-user/git/auto-finance-airflow-pipeline/spark_jobs"
DATA_PATH = "/home/ec2-user/git/auto-finance-airflow-pipeline/data"
OUTPUT_PATH = "/home/ec2-user/git/auto-finance-airflow-pipeline/output"

# BashOperator for running the Spark job
run_spark_job = BashOperator(
    task_id='calculate_loan_risk',
    bash_command=(
        f'{SPARK_HOME}/bin/spark-submit '
        f'{SPARK_JOB_PATH}/calculate_risk.py '
        f'{DATA_PATH}/loan_applications.csv '
        f'{OUTPUT_PATH}/run_{{{{ ts_nodash }}}}'
    ),
    env={
        "SPARK_HOME": SPARK_HOME,
        "SPARK_JOB_PATH": SPARK_JOB_PATH,
        "DATA_PATH": DATA_PATH,
	"OUTPUT_PATH": OUTPUT_PATH
    },
    dag=dag
)
