# Scalable PySpark ETL Framework

This repository contains a generic, configuration-driven ETL framework built on **Apache Spark**. It is designed to showcase senior-level data engineering practices, including distributed data processing, data quality enforcement, and orchestration in a production-like environment.

The framework allows a user to define a complex, multi-step data pipeline in a simple YAML configuration file. It uses PySpark for all data manipulation, making it scalable to handle large datasets. It is designed to be orchestrated by Apache Airflow, and the entire environment—**including a Spark standalone cluster and an Airflow instance**—is containerized with Docker for easy, reproducible setup.

## Framework Architecture

1.  **YAML Configuration**: The user defines the entire pipeline—data sources, transformations, validation rules, and destinations—in a YAML file. This separates the pipeline's logic from its implementation.
2.  **PySpark Engine**: The core orchestrator is a Python script that initializes a `SparkSession`, reads the YAML file, and applies the transformations and validations using the PySpark DataFrame API.
3.  **Modular Transformations & Validations**: The framework comes with a library of reusable PySpark functions for transformations (e.g., `rename_column`, `with_derived_column`) and data validation (e.g., `expect_column_to_exist`, `expect_column_values_to_be_unique`).
4.  **Local Spark & Airflow Cluster**: The `docker-compose.yml` file spins up a complete, multi-container environment:
    * A **Spark Master** node.
    * A **Spark Worker** node.
    * A full **Apache Airflow** instance (webserver, scheduler, worker).
5.  **Airflow `SparkSubmitOperator`**: A sample DAG is provided that uses Airflow's `SparkSubmitOperator` to submit the PySpark job to the standalone cluster, demonstrating a true production orchestration pattern.

## How to Use

### 1. Initialize the Environment

The project includes a setup script to create the necessary directories for Airflow to function correctly inside Docker.

```bash
# Make the script executable
chmod +x setup_airflow.sh

# Run the script
./setup_airflow.sh
