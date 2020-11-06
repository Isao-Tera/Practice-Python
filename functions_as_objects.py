"""
Phenomenal function referencing! 
By adding the functions to a dictionary, 
you can select the function based on the user's input. 
"""
import pandas as pd

df = pd.read_csv("data.csv")

# Function references ot the function map
function_map = {
    'mean': mean,
    'std': std,
    'min': minimum,
    'max': maximum
}

# user input function_name
function_name = input()

# call the chosen function and pass df as an argument
function_map[function_name](df)

"""
Functions as arguments

To pass a function as an argument to another function, 
you had to determine which one you were calling and which one you were referencing. 
Keeping those straight will be important as we dig deeper into this chapter.
"""

def has_docstring(func):
    """Check to see if the function
    'func' has a docstring

    Args:
        func(callable): A function

    Returns:
        bool
    """
    return func.__doc__ is not None

ok = has_docstring(log_product)

if not ok:
    print("The function does not have a docstring")
else:
    print("The function has a docstring")

"""
Nested function
"""
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
