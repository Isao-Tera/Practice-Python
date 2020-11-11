"""
The decorator print_before_and_after() defines a nested function wrapper() 
that calls whatever function gets passed to print_before_and_after(). 

wrapper() adds a little something else to the function call by printing one message 
before the decorated function is called and another right afterwards.

Since print_before_and_after() returns the new wrapper() function, 
we can use it as a decorator to decorate the multiply() function.
"""

def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
  # Return the nested function
    return wrapper

@print_before_and_after
def multiply(a, b):
    print(a * b)

multiply(5, 10)

# Make a decorator
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

"""
Decorate print_sum() with the add_hello() decorator to replicate the issue that the docstring disappears.
Because they are printing the wrapper() function's docstring, not the print_sum() docstring
"""

def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)

# In order to show the doc
# Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().
from functools import wraps 

def add_hello_1(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the modified add_hello() 
@add_hello_1
def print_sum_mod1(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)

print_sum_mod1(10, 20)
print(print_sum_mod1.__doc__)

# decorate wrapper() so that the metadata from func() is preserved in the new decorated function.

def add_hello_add_metadata(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello_add_metadata
def print_sum_mod2(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum_mod2(10, 20)
print(print_sum_mod2.__doc__)


# Measuring overhead of a decorator
def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper