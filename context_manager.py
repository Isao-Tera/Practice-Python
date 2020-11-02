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

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)