"""
Best practice for default arguments
"""
import pandas
# Bad example
def add_column(values, df=pandas.DataFrame()):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
      values (iterable): The values of the new column
      df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

    Returns:
      DataFrame
    """
    df['col_{}'.format(len(df.columns))] = values
    return df

# Try the below code to identify a problem for the bad example
print(add_column(values = range(10)))
print(add_column(values = range(10)))

# Good example
"""
Use an immutable variable for the default argument 
This prevents unexpected behavior like adding multiple columns 
if you call the function more than once.
"""

def better_add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
        If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """
    if df is None:
        df = pandas.DataFrame()
        df['col_{}'.format(len(df.columns))] = values
    return df
