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