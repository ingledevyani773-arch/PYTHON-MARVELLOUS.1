class Demo:
    # Class variable
    Value = 0

    # Parameterized constructor to initialize instance variables
    def __init__(self, val1, val2):
        self.no1 = val1  # Instance variable 1
        self.no2 = val2  # Instance variable 2

    # Instance method Fun
    def Fun(self):
        print(f"Inside Fun - no1: {self.no1}, no2: {self.no2}")

    # Instance method Gun
    def Gun(self):
        print(f"Inside Gun - no1: {self.no1}, no2: {self.no2}")


# Creating two objects of the Demo class
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling the instance methods in the specified sequence
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()