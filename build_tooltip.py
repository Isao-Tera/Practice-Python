"""
Displays a tooltip with a function's docstring
Complete the build_tooltip() function 
that retrieves a docstring from an arbitrary function.
"""

import inspect 

def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)
  #return print(f"{border}\n{docstring}\n{border}")
