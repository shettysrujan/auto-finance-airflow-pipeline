from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="auto_finance_risk_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_spark_job = BashOperator(
        task_id="calculate_loan_risk",
        bash_command="spark-submit /home/ec2-user/git/auto-finance-airflow-pipeline/spark_jobs/calculate_risk.py"
    )
