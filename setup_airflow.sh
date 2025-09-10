#!/bin/bash

# Create necessary directories for Airflow
mkdir -p ./airflow/dags
mkdir -p ./airflow/logs
mkdir -p ./airflow/plugins

# Create an empty requirements file for Airflow if it doesn't exist
# This allows us to add specific dependencies for the Airflow environment
touch ./airflow/requirements.txt

echo "Airflow directories and files created successfully."
echo "You can now run 'docker-compose up -d'."
