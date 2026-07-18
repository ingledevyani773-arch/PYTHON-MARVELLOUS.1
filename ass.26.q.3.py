class Arithmetic:
    def __init__(self):
        # Initialize instance variables to 0
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        # Accept values from the user
        try:
            self.Value1 = float(input("Enter the first value (Value1): "))
            self.Value2 = float(input("Enter the second value (Value2): "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            self.Value1 = 0
            self.Value2 = 0

    def Addition(self):
        # Return the sum of Value1 and Value2
        return self.Value1 + self.Value2

    def Subtraction(self):
        # Return the difference of Value1 and Value2
        return self.Value1 - self.Value2

    def Multiplication(self):
        # Return the product of Value1 and Value2
        return self.Value1 * self.Value2

    def Division(self):
        # Return the division result, handling division by zero safely
        if self.Value2 == 0:
            return "Error: Division by zero is not allowed."
        return self.Value1 / self.Value2


# --- Main Demonstration ---

print("--- Operating on Object 1 ---")
obj1 = Arithmetic()
obj1.Accept()

print(f"Addition: {obj1.Addition()}")
print(f"Subtraction: {obj1.Subtraction()}")
print(f"Multiplication: {obj1.Multiplication()}")
print(f"Division: {obj1.Division()}")

print("\n--- Operating on Object 2 (Testing Division by Zero) ---")
obj2 = Arithmetic()
obj2.Accept()

print(f"Addition: {obj2.Addition()}")
print(f"Subtraction: {obj2.Subtraction()}")
print(f"Multiplication: {obj2.Multiplication()}")
print(f"Division: {obj2.Division()}")