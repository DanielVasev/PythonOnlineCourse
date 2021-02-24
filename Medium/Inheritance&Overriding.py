# Generating class
class Parents:

    def my_first_name(self, name):
        print(name)


"""
    Generating second class which inherithance the first class.
    As we typing first class name in the brackets in the second class
"""


class Child(Parents):
    def my_last_name(self, sname):
        print(sname)


"""
    his function is the same as the one in parent class and override with new value "pepka" instead of "Daniel"
    Uncomment to see the difference
"""


def my_first_name(self):
    print("Pepka")


daniel = Child()
daniel.my_first_name("Daniel")
daniel.my_last_name("Perov")
