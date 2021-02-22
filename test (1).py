# Databricks notebook source
# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %sh ls

# COMMAND ----------

# MAGIC %pip install mlflow

# COMMAND ----------

import train
train.main()


# COMMAND ----------

import pandas
input_df = pandas.read_csv("wine-quality.csv")
display(input_df)

# COMMAND ----------

def foo():
  return open("wine-quality.csv").read()
sc.parallelize(range(0, 1)).map(lambda x: foo()).collect()


# COMMAND ----------

# doesn't work
spark.read.format("csv").load("file:/Workspace/Repos/kahing.cheung@databricks.com/mlflow-example/wine-quality.csv").collect()

