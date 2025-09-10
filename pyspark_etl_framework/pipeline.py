import yaml
import argparse
from pyspark.sql import SparkSession
from pyspark_etl_framework import transformations, validators

class Pipeline:
    """A class to orchestrate a PySpark ETL pipeline from a YAML config."""

    def __init__(self, config_path: str):
        """
        Initializes the Pipeline with a path to a YAML configuration file.
        """
        print(f"Initializing pipeline with config: {config_path}")
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        pipeline_name = self.config.get('name', 'pyspark-etl-pipeline')
        print(f"Starting Spark session for pipeline: {pipeline_name}")
        self.spark = SparkSession.builder.appName(pipeline_name).getOrCreate()

    def run(self):
        """
        Executes the entire ETL pipeline defined in the config.
        """
        try:
            for step in self.config['pipeline']:
                step_name = step['name']
                print(f"--- Executing step: {step_name} ---")
                
                if step_name == 'extract':
                    self.df = self._extract(step['details'])
                elif step_name == 'transform':
                    self.df = self._transform(self.df, step['details'])
                elif step_name == 'validate':
                    self._validate(self.df, step['details'])
                elif step_name == 'load':
                    self._load(self.df, step['details'])
                else:
                    raise ValueError(f"Unknown step: {step_name}")
        finally:
            print("Stopping Spark session.")
            self.spark.stop()

    def _extract(self, details: dict):
        """Handles the data extraction step."""
        source_type = details['type']
        if source_type == 'csv':
            path = details['path']
            print(f"Reading CSV from: {path}")
            return self.spark.read.csv(path, header=True, inferSchema=True)
        else:
            raise ValueError(f"Unsupported extract type: {source_type}")

    def _transform(self, df, details: list):
        """Handles the data transformation step by applying a series of functions."""
        for transform_step in details:
            func_name = transform_step['function']
            args = transform_step.get('args', {})
            print(f"Applying transformation: {func_name} with args: {args}")
            transform_func = getattr(transformations, func_name)
            df = transform_func(df, **args)
        return df

    def _validate(self, df, details: list):
        """Handles the data validation step."""
        for validation_step in details:
            func_name = validation_step['function']
            args = validation_step.get('args', {})
            print(f"Applying validation: {func_name} with args: {args}")
            validation_func = getattr(validators, func_name)
            validation_func(df, **args)
        print("All validations in this step passed successfully.")

    def _load(self, df, details: dict):
        """Handles the data loading step."""
        dest_type = details['type']
        if dest_type == 'parquet':
            path = details['path']
            mode = details.get('mode', 'overwrite')
            print(f"Writing DataFrame to Parquet at: {path} with mode: {mode}")
            df.write.mode(mode).parquet(path)
        elif dest_type == 'console':
            print("Displaying final DataFrame to console:")
            df.show(truncate=False)
        else:
            raise ValueError(f"Unsupported load type: {dest_type}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a PySpark ETL pipeline.")
    parser.add_argument('--config', required=True, help="Path to the pipeline YAML config file.")
    args = parser.parse_args()

    pipeline = Pipeline(config_path=args.config)
    pipeline.run()
