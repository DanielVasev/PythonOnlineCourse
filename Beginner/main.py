# import tuna module
from Beginner import tuna

# import random module
import random

# add for loo[ with range of 10
for a in range(10):
    #generating a random number between 50 , 59
    result = x = random.randrange(50, 59)

    #printing the generated number
    print(result)

# looking for specific number which will stop the program
    if result == 56:
        print("this is the magic number")
        break
    else:
        print("carry on!")





print(tuna.print_fName("Daniel ") + tuna.print_sName("Vasev"))