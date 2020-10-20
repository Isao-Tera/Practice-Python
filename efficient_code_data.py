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
print(both)

# Find the Pokémon that Ash has, and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

# Extract uniqe value from a list
uniue_names_set = set(names)

# Using for loop to extract unique value
def find_unique_name(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names
