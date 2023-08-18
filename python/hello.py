import random
from statistics import mean

# Create a new list of 100 random numbers from 0 to 1000 using random.sample method.
list = random.sample(range(0, 1000), 100)

# Sorting the list using For loop by comparing all elements with each other.
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]

# Create two new list. One list that will contain even numbers, and second list for odd numbers.
even = []
odd = []

# Verify if a number is even or odd and assign it to a corresponding list.
for i in range(len(list)):
    if (list[i] % 2) == 0:
        even.append(list[i])
    else:
        odd.append(list[i])

# Calculate average from even and odd numbers using mean formula and printing the results.
# https://statisticsbyjim.com/basics/mean_average/
print(mean(even))
print(mean(odd))
