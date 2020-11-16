#Generating class
class Parents():
    def my_first_name(self):
        print("Daniel")

#Generating second class which inherithance the first class like typing first class name in the brackets in the second class
class Child(Parents):
    def my_last_name(self):
        print("Vasev")

        # this function is the same as the one in parent class and override with new value "pepka" instead of "Daniel"
        #Uncoment to see the difference
    #def my_first_name(self):
     #   print("Pepka")


daniel = Child()
daniel.my_first_name()
daniel.my_last_name()












