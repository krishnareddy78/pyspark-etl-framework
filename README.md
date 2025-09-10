# ⚡ Scalable PySpark ETL Framework

This repository contains a **generic, configuration-driven ETL framework** built on **Apache Spark**.  
It is designed to showcase **senior-level data engineering practices**, including:

- Distributed data processing
- Data quality enforcement
- Orchestration in a production-like environment

The framework allows a user to define a **complex, multi-step data pipeline** in a simple **YAML configuration file**.  
It uses **PySpark** for all data manipulation, making it scalable to handle large datasets.  

It is designed to be orchestrated by **Apache Airflow**, and the entire environment—including a **Spark standalone cluster** and an **Airflow instance**—is containerized with **Docker** for easy, reproducible setup.

---

## 🏛️ Framework Architecture

- **YAML Configuration**  
  The user defines the entire pipeline—data sources, transformations, validation rules, and destinations—in a YAML file.  
  This separates the pipeline's logic from its implementation.

- **PySpark Engine**  
  The core orchestrator is a Python script that initializes a `SparkSession`, reads the YAML file, and applies transformations and validations using the **PySpark DataFrame API**.

- **Modular Transformations & Validations**  
  Includes a library of reusable PySpark functions:
  - Transformations: `rename_column`, `with_derived_column`, etc.  
  - Validations: `expect_column_to_exist`, `expect_column_values_to_be_unique`, etc.

- **Local Spark & Airflow Cluster** (via `docker-compose`)  
  - Spark Master node  
  - Spark Worker node  
  - Full Apache Airflow instance (webserver, scheduler, worker)

- **Airflow Orchestration**  
  A sample DAG is provided that uses **Airflow's `SparkSubmitOperator`** to submit the PySpark job to the standalone cluster, demonstrating a **production-grade orchestration pattern**.

---

## 🚀 How to Use

### 1. Initialize the Environment
Run the setup script to create the necessary directories for Airflow to function correctly inside Docker.

```bash
chmod +x setup_airflow.sh
./setup_airflow.sh

2. Launch the Spark & Airflow Cluster
This single command will build and start all services.
docker-compose up -d
Airflow UI → http://localhost:8080 (login: airflow/airflow)
Spark Master UI → http://localhost:8081
3. Trigger the ETL Pipeline via Airflow
Open the Airflow UI in your browser.
Find the DAG named pyspark_etl_sales_pipeline.
Enable the DAG and click ▶ Play to trigger a run.
Monitor execution in the Grid View and inspect logs from the SparkSubmitOperator.
