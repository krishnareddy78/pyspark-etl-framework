from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr

def rename_column(df: DataFrame, old_name: str, new_name: str) -> DataFrame:
    """
    Renames a column in the DataFrame.

    Args:
        df: The input PySpark DataFrame.
        old_name: The current name of the column.
        new_name: The desired new name of the column.

    Returns:
        A new DataFrame with the column renamed.
    """
    print(f"Renaming column '{old_name}' to '{new_name}'")
    return df.withColumnRenamed(old_name, new_name)

def drop_columns(df: DataFrame, columns: list) -> DataFrame:
    """
    Drops one or more columns from the DataFrame.

    Args:
        df: The input PySpark DataFrame.
        columns: A list of column names to drop.

    Returns:
        A new DataFrame with the specified columns removed.
    """
    print(f"Dropping columns: {columns}")
    return df.drop(*columns)

def with_derived_column(df: DataFrame, new_column_name: str, expression: str) -> DataFrame:
    """
    Adds a new column to the DataFrame based on a SQL-like expression.

    Args:
        df: The input PySpark DataFrame.
        new_column_name: The name of the new column to create.
        expression: A Spark SQL expression to calculate the new column's value
                    (e.g., "quantity * unit_price").

    Returns:
        A new DataFrame with the derived column.
    """
    print(f"Adding derived column '{new_column_name}' with expression: '{expression}'")
    return df.withColumn(new_column_name, expr(expression))

def cast_column(df: DataFrame, column_name: str, new_type: str) -> DataFrame:
    """
    Casts a column to a new data type.

    Args:
        df: The input PySpark DataFrame.
        column_name: The name of the column to cast.
        new_type: The target data type (e.g., 'integer', 'double', 'timestamp').

    Returns:
        A new DataFrame with the column cast to the new type.
    """
    print(f"Casting column '{column_name}' to type '{new_type}'")
    return df.withColumn(column_name, col(column_name).cast(new_type))
