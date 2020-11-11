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

