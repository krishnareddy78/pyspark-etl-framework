from pyspark.sql import DataFrame

class ValidationError(Exception):
    """Custom exception for data validation failures."""
    pass

def expect_column_to_exist(df: DataFrame, column_name: str):
    """
    Checks if a column exists in the DataFrame.

    Args:
        df: The input PySpark DataFrame.
        column_name: The name of the column to check for.

    Raises:
        ValidationError: If the column does not exist.
    """
    print(f"Validating existence of column: '{column_name}'")
    if column_name not in df.columns:
        raise ValidationError(f"Validation failed: Column '{column_name}' not found in DataFrame.")

def expect_column_values_to_be_unique(df: DataFrame, column_name: str):
    """
    Checks if all values in a column are unique.

    Args:
        df: The input PySpark DataFrame.
        column_name: The name of the column to check for uniqueness.

    Raises:
        ValidationError: If the column contains duplicate values.
    """
    print(f"Validating uniqueness of column: '{column_name}'")
    count = df.count()
    distinct_count = df.select(column_name).distinct().count()

    if count != distinct_count:
        raise ValidationError(f"Validation failed: Column '{column_name}' contains duplicate values.")

def expect_column_values_to_not_be_null(df: DataFrame, column_name: str):
    """
    Checks if a column contains any null values.

    Args:
        df: The input PySpark DataFrame.
        column_name: The name of the column to check for nulls.

    Raises:
        ValidationError: If the column contains null values.
    """
    print(f"Validating no nulls in column: '{column_name}'")
    null_count = df.where(df[column_name].isNull()).count()

    if null_count > 0:
        raise ValidationError(f"Validation failed: Column '{column_name}' contains {null_count} null values.")

def expect_row_count_to_be_between(df: DataFrame, min_value: int, max_value: int):
    """
    Checks if the total row count of the DataFrame is within a specified range.

    Args:
        df: The input PySpark DataFrame.
        min_value: The minimum acceptable row count.
        max_value: The maximum acceptable row count.
    
    Raises:
        ValidationError: If the row count is outside the specified range.
    """
    print(f"Validating row count to be between {min_value} and {max_value}")
    count = df.count()
    if not (min_value <= count <= max_value):
        raise ValidationError(f"Validation failed: Row count {count} is not between {min_value} and {max_value}.")
