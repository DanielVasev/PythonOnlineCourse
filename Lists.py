'''List of integers'''
results = 0
numbers = [23,55,66,79,56]
print(numbers[1])
print(numbers[2] + numbers[0])


'''list of strings'''
names = ["ina" , "vasq", 23, "petka"]

print(names)

'''add temporary items'''
print(numbers + [33,44,55])

newNumbers = numbers + [33,44,55]
print(numbers)
print(newNumbers)

'''add item permanantly'''
numbers.append(33)
print(numbers)


'''slice the list'''
print(numbers)
print(numbers[1:3])
