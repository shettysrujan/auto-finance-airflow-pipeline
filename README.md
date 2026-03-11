# Auto Finance Loan Risk Pipeline

A simple Data Engineering project using **Apache Airflow + PySpark**.

The pipeline processes loan applications and calculates a basic credit risk level.

---

## Architecture

EC2
│
├── Apache Airflow
│    ├── Scheduler
│    ├── Webserver
│
├── PySpark
│
└── PostgreSQL (Airflow metadata database)

---

## Project Structure

```
auto-finance-airflow-pipeline
│
├── dags
│   └── loan_risk_pipeline.py
│
├── spark_jobs
│   └── calculate_risk.py
│
├── data
│   └── loan_applications.csv
│
└── output
```

---

## Pipeline Flow

1. Airflow scheduler detects the DAG
2. DAG triggers a Spark job
3. Spark processes loan applications
4. Risk level is calculated
5. Results are stored in output folder

---

## Sample Data

| application_id | customer_name | credit_score | income | loan_amount |
|---|---|---|---|---|
| 1 | John | 720 | 90000 | 25000 |

---

## Risk Logic

```
credit_score >= 700 → LOW
credit_score >= 600 → MEDIUM
else → HIGH
```

---

## Running the Project

Start Airflow:

```
airflow scheduler
airflow webserver --port 8080
```

Open UI:

```
http://<EC2-IP>:8080
```

Trigger DAG:

```
auto_finance_risk_pipeline
```

---

## Output Example

```
application_id,customer_name,risk_level
1,John,LOW
2,Alice,HIGH
3,Bob,MEDIUM
```

---

## Tech Stack

- Apache Airflow
- PySpark
- AWS EC2
- PostgreSQL
- Git
