#Pokemon names
names = ['Abomasnow',
 'Abra',
 'Absol',
 'Accelgor',
 'Aerodactyl',
 'Aggron',
 'Aipom',
 'Alakazam',
 'Alomomola',
 'Altaria'
]

#Pokemon types
primary_types = ['Grass','Psychic','Dark','Bug','Rock','Steel','Normal','Psychic','Water','Dragon']

secondary_types = ['Ice',
 "nan",
 "nan",
 "nan",
 'Flying',
 'Rock',
 "nan",
 "nan",
 "nan",
 'Flying',
]

"""
combine all three lists into one list
"""#
names_type = [*zip(names, primary_types, secondary_types)]
#print(names_type[5])

# Easier and Faster way to count
from collections import Counter

#Example 1
type_counter = Counter(primary_types)
#print(type_counter)

#Example 2
last_letters = [name[-1] for name in names]
last_letters_count = Counter(last_letters)
#print(last_letters_count)

"""
Make combinations
"""
from itertools import combinations
pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
#print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
#print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon,4)]
#print(combos_4)

"""
set 
"""
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
#print(both)

# Find the Pokémon that Ash has, and Misty does not have
ash_only = ash_set.difference(misty_set)
#print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
#print(unique_to_set)

# Extract uniqe value from a list
uniue_names_set = set(names)

# Using for loop to extract unique value
def find_unique_name(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names


"""
Eliminating loops from the code
"""
poke_gens = [4,1,3,5,1,3,2,1,5,6]
poke_names = [
 'Abomasnow',
 'Abra',
 'Absol',
 'Accelgor',
 'Aerodactyl',
 'Aggron',
 'Aipom',
 'Alakazam',
 'Alomomola',
 'Altaria']

# make name and generation pair by for loop
gen1_gen2_name_length_loop = []
for name, gen in zip(poke_names, poke_gens):
    if gen < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_length_loop.append(poke_tuple)
#print(gen1_gen2_name_length_loop)

# Using list complihension

## 1. extract pokemon name for gen1 and gen2 as a list 
gen1_gen2_list = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]
#print(gen1_gen2_list)

## 2. calculate length of name 
gen1_gen2_name_length = [*map(len, gen1_gen2_list)]
#print(gen1_gen2_name_length)

## 3. Add 1 and 2
gen1_gen2_name_length_cono = [zip(gen1_gen2_list, gen1_gen2_name_length)]

"""
Calculate total and average without loops
"""
import numpy as np
stats_list = [[10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60],
              [10, 20, 30, 40, 50, 60]]

stats = np.array(stats_list)

# pokemon name and status combinataion when using loop
poke_list = []
for name, num in zip(names, stats):
    total_stats = np.sum(num)
    avg_stats = np.mean(num)
    poke_list.append(name, total_stats, avg_stats)

# No loop
# Create a total stats array
total_stats_np = np.sum(stats, axis=1)

# Create an average stats array
avg_stats_np = np.mean(stats, axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

"""
improve loop efficiency
"""
from collections import Counter
generations = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3, 6, 4, 5, 2, 3, 1, 1, 4, 5, 
5, 2, 3, 6, 3, 1, 5, 6, 6, 5, 4, 2, 3, 3, 3, 3, 6, 3, 5, 4, 2, 5, 3, 1, 
5, 3, 2, 1, 6, 4, 4, 6, 5, 1, 3, 2, 5, 5, 4, 5, 6, 5, 3, 4, 4, 4, 4, 1, 
4, 6, 4, 1, 3, 3, 3, 6, 4, 5, 3, 3, 3, 1, 2, 5, 1, 1, 1, 1, 4, 4, 4, 6, 
6, 2, 4, 3, 2, 4, 5, 3, 6, 6, 3, 1, 1, 2, 1, 5, 5, 4, 3, 5, 3, 2, 5, 3, 
4, 3, 4, 4, 2, 2, 5, 5, 5, 1, 2, 4, 5, 5, 5, 6, 5, 5, 3, 2, 6, 1, 5, 4, 
6, 6, 1, 1, 1, 1, 2, 6, 6, 1, 1, 4, 1, 4, 4, 5, 1, 5, 5, 1, 2, 5, 5, 3, 
4, 3, 3, 5, 5, 5, 1, 1, 1, 4, 3, 1, 2, 5, 5, 5, 4, 2, 5, 2, 6, 5, 1, 1, 
3, 1, 1, 3, 6, 2, 5, 5, 4, 2, 6, 1, 6, 6, 4, 6, 6, 3, 5, 2, 5, 5, 6, 6, 
4, 6, 2, 4, 4, 5, 5, 4, 3, 1, 4, 5, 1, 1, 4, 5, 2, 4, 3, 4, 2, 4, 1, 6, 
1, 1, 1, 1, 5, 5, 6, 6, 3, 5, 5, 5, 2, 1, 6, 1, 4, 3, 3, 3, 1, 3, 3, 5, 
1, 4, 3, 1, 6, 5, 5, 4, 6, 6, 2, 5, 4, 4, 1, 1, 2, 2, 4, 6, 2, 2, 1, 2, 
2, 3, 5, 1, 2, 3, 4, 6, 1, 5, 1, 3, 1, 5, 2, 1, 1, 1, 1, 1, 1, 5, 3, 2, 
1, 3, 5, 6, 5, 5, 1, 1, 4, 4, 5, 5, 3, 3, 5, 5, 5, 3, 5, 2, 1, 5, 2, 3, 
3, 4, 5, 2, 2, 4, 1, 5, 3, 5, 5, 3, 6, 5, 3, 4, 3, 3, 4, 3, 2, 4, 3, 3, 
4, 4, 1, 1, 1, 2, 2, 1, 1, 4, 1, 1, 4, 3, 6, 4, 4, 5, 3, 1, 2, 4, 5, 2, 
2, 1, 3, 3, 3, 3, 3, 6, 6, 1, 4, 3, 3, 1, 1, 1, 5, 5, 3, 3, 2, 4, 5, 3, 
2, 4, 1, 4, 4, 1, 3, 1, 4, 5, 2, 5, 2, 1, 1, 1, 1, 1, 1, 3, 1, 3, 2, 6, 
6, 3, 3, 3, 2, 1, 1, 1, 1, 5, 4, 4, 5, 6, 6, 5, 5, 5, 1, 1, 5, 5, 3, 1, 
5, 2, 6, 4, 2, 1, 1, 1, 5, 5, 1, 2, 2, 1, 4, 3, 2, 1, 1, 1, 1, 3, 1, 4, 
2, 1, 4, 4, 1, 2, 5, 4, 6, 2, 2, 6, 2, 1, 2, 3, 4, 1, 1, 1, 3, 3, 4, 3, 
3, 3, 2, 5, 5, 1, 1, 4, 4, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 3, 3, 5, 5, 1, 
1, 5, 5, 6, 3, 2, 5, 5, 5, 1, 1, 1, 3, 3, 1, 5, 2, 5, 5, 3, 5, 3, 3, 3, 
1, 4, 5, 4, 3, 4, 3, 2, 3, 5, 3, 5, 5, 5, 2, 6, 2, 3, 4, 6, 4, 3, 3, 6]

# Collect the count of each generation
gen_counts = Counter(generations)

# Improve for loop by moving one calculation above the loop
total_count = len(generations)

for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))
