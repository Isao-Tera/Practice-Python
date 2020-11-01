"""
Practice writing docstring when making a function
"""

def standardize(column):
    """Standardize the values in a column.

    Args:
      column (pandas Series): The data to standardize.

    Returns:
      pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score

"""
Do the one thing in a function
"""

# bad example
def mean_and_median(values):
  """Get the mean and median of a list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median

# Good example
def mean(values):
    """Get the mean of a list of values
      
    Args:
        values(iterable of float):A list of numbers

    Returns
        values(float): the mean
    """
    mean = sum(values) / len(values)
    return mean

def median(values):
  """Get the median of a list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  midpoint = int(len(values / 2))
  if len(values) % 2 == 0:
    median = (values[midpoint -1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median