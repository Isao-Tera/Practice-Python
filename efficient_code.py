# Non-pythonic code
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
#print(new_list)

# Better but non-pythonic
"""
more pythonic approch would loop over the contents rather than using index variable
"""

better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
#print(better_list)

# Pythonic
best_list = [name for name in names if len(name) >= 6]
#print(best_list)

# Bilut-In function

# Create a range object that goes from 0 to 5
nums = range(6)

# Convert nums to a list
nums_list = list(nums)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object using * charactor
nums_list2 = [*range(1,12,2)]

"""Built-in practice ; enumerate()"""
indexed_name = []
# No enumerate()
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_name.append(index_name)
#print(indexed_name)

# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
#print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i,name in enumerate(names)]
#print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
#print(indexed_names_unpack)

"""Built-in practice:map()"""
# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
#print(names_map)
#print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
#print(names_uppercase)

"""Numpy practice"""
import numpy as np
numbers_list = [[1,2,3,4,5],
                [6,7,8,9,10]]
nums = np.array(numbers_list)
print(nums)

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

""""Bring knowledge all together"""
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

"""
We should time to write more efficient code.
To do that, use magic code '%timeit' in front of code at the iPython shell or Jupyter
"""
#Example codes
%timeit formal_list = list()
%timeit literal_list = []

"""
literal_list; 47.3 ns ± 5.37 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
formal_list; 138 ns ± 14.6 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
Making literal list is faster than making formal one
"""
"""
time for one line code : %timeit
time for multiple lines code : %%timeit
"""

"""
Identify code time performance
using %lprun
"""
import line_profiler
import numpy as np
heroes = ['A-Bomb', 'Abe Sapien', 'Abin Sur', 'Abomination', 'Absorbing Man', 
          'Adam Strange', 'Agent 13', 'Agent Bob', 'Agent Zero', 'Air-Walker']
hts_list = [203. , 191. , 185. , 203. , 193. , 185. , 173. , 178. , 191. ,188.]
wts_list = [441.,  65.,  90., 441., 122.,  88.,  61.,  81., 104., 108.]

hts = np.array(hts_list)
wts = np.array(wts_list)

# Prepare a function to profile
def convert_units(heroes, weight, height):
    """
    convert units from lbs to ISO

    Arguments:
    heroes : name of hero
    weight: weight of hero
    height: height of hero

    Returns:
    hero_data: index and converted data
    """

    new_hts = [ht * 0.39370 for ht in height]
    new_wts = [wt * 2.20462 for wt in weight]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

"""
To profile the convert_units(), use below 

%load_ext line_profiler
%lprun -f convert_units convert_units(heroes,wts,hts)
"""

# Modify the function by changing bottleneck
def convert_units_broadcast(heroes, weight, height):
    """
    convert units from lbs to ISO

    Arguments:
    heroes : name of hero
    weight: weight of hero
    height: height of hero

    Returns:
    hero_data: index and converted data
    """

    # Change list comprihension to np.array 
    new_hts = height * 0.39370
    new_wts = weight * 2.20462 

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

"""
To profile memory usage in the code
Use memory_profiler
"""
import memory_profiler

#before using memory_profiler, import a function to be profiled
from convert_unit import convert_units

"""
When using memory_profiler, execute below code in the Jupyter or iPyhotn shell 
%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes, wts, hts)
"""
