import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("LoanRisk").getOrCreate()

input_csv = sys.argv[1]
output_path = sys.argv[2]  # now passed from Airflow

df = spark.read.csv(input_csv, header=True, inferSchema=True)

df = df.withColumn(
    "risk_level",
    when(df.credit_score >= 700, "LOW")
    .when(df.credit_score >= 600, "MEDIUM")
    .otherwise("HIGH")
)

df.write.mode("overwrite").csv(output_path, header=True)
spark.stop()
