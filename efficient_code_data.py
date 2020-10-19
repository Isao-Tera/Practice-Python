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

# combine all three lists into one list
names_type = [*zip(names, primary_types, secondary_types)]
print(names_type[5])

# Easier and Faster way to count
from collections import Counter

#Example 1
type_counter = Counter(primary_types)
print(type_counter)

#Example 2
last_letters = [name[-1] for name in names]
last_letters_count = Counter(last_letters)
print(last_letters_count)