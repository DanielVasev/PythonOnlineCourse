#Create class with name Tuna
class Tuna:
    # 2 input fields tranforming string to integer
    number1 = int(input("add 1 number!\n"))
    number2 = int(input("add 2 number!\n"))

#init will be exsecuted once class is in use
    def __init__(self):
        print("Hi there lets start!")

#Simple function
    def count(self):
        sum = self.number2 + self.number1
        print(sum)

#Creating instance (object) of out Tuna class
count = Tuna()
count.count()