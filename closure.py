"""
the values that we passed to return_a_func() are still accessible to the new function she returned, 
even after the program has left the scope of return_a_func()

Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2), 
but only if they are used in the nested function. 
That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), 
then it would not be captured in new_func()'s closure.
"""

def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))
    return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])