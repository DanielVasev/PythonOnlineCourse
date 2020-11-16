def training_function(name = "Daniel", action = "sleeping", what = "noisy"):
    print(name, action, what)


training_function(name = "Reni", action="fart")


# Flexible Number of Arguments
print("Flexible Argument")

def add_number(*args):
    result = 0
    for a in args:
        result += a
    print(result)

add_number(33,33,33)
add_number(43, 5435345,345345366)
add_number(33,33,33)

# Unpack Arguments
print("Age Calculator results")
def age_calculator(age, apples_eat, cig_smoke):
    result = (100 - age) + (apples_eat * 3.5) - (cig_smoke *2)
    print(result)

daniel_data = [38,2,0]
vasia_data = [34,0,1000]

age_calculator(daniel_data[0],daniel_data[1],daniel_data[2])
age_calculator(*vasia_data)