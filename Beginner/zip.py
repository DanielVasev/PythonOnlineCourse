"""
Use ZIP function to join 2 lists

"""

# First list
firstNames = ["Daniel", "Ina", "Mali"]

# Second list
lastNames = ["Vasev", "Rujekova", "Vaseva"]

# We using zip to join both lists
names = zip(firstNames, lastNames)

# Option 1 to see the result
for a,b in names:
    print(a,b)

# Option 2 to see the result
print(*names)