import random
import string

# Choose a random number of dictionaries inside a list.
n = random.randrange(2, 10, 1)

# Create a new, empty list.
list_one = []

# Using nested loop to create list of dictionaries. Inner loop, that creates a dictionary with 3 key:values pairs.
# Key:value pair consists of a random letter key and random number value.
# Outer loop, that creates n new dictionaries and add them to the list.

for i in range(n):
    my_dict = {}
    list_one.append(my_dict)
    for j in range(3):
        my_dict[random.choice(string.ascii_lowercase)] = random.randrange(0, 100, 1)

# Print generated list of dictionaries.
print(list_one)

# Create one common dictionary and removing duplicated keys.
new_dictionary = {}
for k in range(n):
    for k, v in list_one[k].items():
        if k in new_dictionary and v >= new_dictionary[k]:
            new_dictionary[k + '_2'] = v
            del new_dictionary[k]
        elif k in new_dictionary and v <= new_dictionary[k]:
            new_dictionary[k + '_1'] = new_dictionary[k]
            del new_dictionary[k]
        elif k not in new_dictionary:
            new_dictionary[k] = v
        else:
            continue

# Print new dictionary.
print(new_dictionary)

