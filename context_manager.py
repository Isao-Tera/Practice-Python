"""
By opening the file using the with open() statement,
you were able to read in the text of the file. More importantly,
when you were done reading the text, 
the context manager closed the file for you.
"""

# Practice using context manager 
# Open "alice.txt" and assign the file to "file"
with  open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

"""
there was no as <variable name> at the end of the with statement in timer() context manager. 
That is because timer() is a context manager that does not return a value, 
so the as <variable name> at the end of the with statement isn't necessary.
"""
image = get_image_from_instagram()
import time
import contextlib
"""
the three elements of a context manager are all here: 
a function definition, 
a yield statement, 
and the @contextlib.contextmanager decorator.
"""

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)


"""
It is OK to use nested with statement.
Nesting context managers like this allows you 
to connect to the stock market (the CONNECT/DISCONNECT pattern) 
and write to a file (the OPEN/CLOSE pattern) at the same time.
"""
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock("NVDA") as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open("NVDA.txt", "w")  as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

"""
Control tasks in a context manager
using try-except-finally
"""
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)