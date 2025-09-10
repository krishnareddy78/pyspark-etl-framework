from airflow.decorators import dag
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

@dag(
    dag_id='pyspark_etl_sales_pipeline',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['pyspark', 'etl'],
)
def pyspark_etl_dag():
    """
    This DAG runs a PySpark ETL job defined by a YAML configuration file.
    """
    SparkSubmitOperator(
        task_id='submit_pyspark_etl_job',
        application='/opt/airflow/pyspark_etl_framework/pipeline.py',  # Path to the main script in the Airflow container
        conn_id='spark_default',  # The connection configured for the Spark Master
        application_args=['--config', '/opt/airflow/pipelines/sales_pipeline.yml'],
        conf={
            "spark.master": "spark://spark-master:7077",
        },
    )

pyspark_etl_dag()
