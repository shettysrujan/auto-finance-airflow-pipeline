from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = SparkSession.builder.appName("LoanRisk").getOrCreate()

df = spark.read.csv("data/loan_applications.csv", header=True, inferSchema=True)

df = df.withColumn(
    "risk_level",
    when(df.credit_score >= 700, "LOW")
    .when(df.credit_score >= 600, "MEDIUM")
    .otherwise("HIGH")
)

df.write.mode("overwrite").csv("output/loan_risk_results", header=True)

spark.stop()
