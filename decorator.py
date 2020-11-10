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