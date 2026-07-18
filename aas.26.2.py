class Circle:
    # Class variable
    PI = 3.14

    # Constructor initializing instance variables to 0.0
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Method to accept radius from the user
    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    # Method to calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    # Method to calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Method to display all values
    def Display(self):
        print(f"Radius        : {self.Radius}")
        print(f"Area          : {self.Area:.2f}")
        print(f"Circumference : {self.Circumference:.2f}")
        print("-" * 30)


# Main code execution with multiple objects
if __name__ == "__main__":
    print("--- Circle Object 1 ---")
    obj1 = Circle()  # Creating first object
    obj1.Accept()  # Accepting input
    obj1.CalculateArea()  # Calculating Area
    obj1.CalculateCircumference()  # Calculating Circumference
    obj1.Display()  # Displaying results

    print("--- Circle Object 2 ---")
    obj2 = Circle()  # Creating second object
    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()