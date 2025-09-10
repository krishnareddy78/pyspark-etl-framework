# Scalable ETL and Data Pipeline Framework

This repository contains a generic, configuration-driven ETL (Extract, Transform, Load) framework built in Python. It is designed to demonstrate data engineering best practices, including modularity, data quality enforcement, and orchestration. This project proves an ability to build the foundational tools that enable data science, rather than just using them.

The framework allows a user to define a complex, multi-step data pipeline in a simple YAML configuration file. It integrates `pandera` for rigorous data validation and is designed to be orchestrated by tools like Apache Airflow.

## Framework Architecture

1.  **YAML Configuration**: The user defines the entire pipeline—including data sources, transformations, validation rules, and destinations—in a YAML file. This separates the pipeline's logic from its implementation.
2.  **Pipeline Orchestrator**: A core `Pipeline` class reads the YAML file, initializes the necessary tasks, and executes them in the specified order.
3.  **Modular Tasks**: The framework is built on a series of abstract base classes for each ETL step (`ExtractTask`, `TransformTask`, `ValidateTask`, `LoadTask`), making it easily extensible.
4.  **Schema Enforcement**: At any point in the pipeline, a `ValidateTask` can be added to enforce a data schema using `pandera`, ensuring data quality and preventing corrupted data from moving downstream.
5.  **Airflow & Docker Integration**: The project includes a `docker-compose.yml` file to spin up a local Apache Airflow instance. A sample DAG is provided to show how to schedule and run a pipeline defined by this framework.

## How to Use

### 1. Run a Pipeline Locally

You can run any pipeline directly using the framework's entry point.

```bash
# Install dependencies
pip install -r requirements.txt

# Run the example sales pipeline
python -m etl_framework.pipeline --config pipelines/sales_pipeline.yml
