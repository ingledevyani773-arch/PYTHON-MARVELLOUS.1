class Numbers:
    def __init__(self, value):
        """Initializes the instance variable with an integer value."""
        self.Value = int(value)

    def ChkPrime(self):
        """Returns True if the number is prime, otherwise False."""
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        """Returns True if the number is perfect, otherwise False.
        A perfect number equals the sum of its proper divisors."""
        if self.Value <= 1:
            return False
        sum_divisors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_divisors += i
        return sum_divisors == self.Value

    def Factors(self):
        """Displays all factors of the number."""
        factors_list = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_list.append(i)
        print(f"Factors of {self.Value}: {factors_list}")

    def SumFactors(self):
        """Returns the sum of all factors."""
        sum_total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum_total += i
        return sum_total


# --- Creating multiple objects and calling all methods ---

# Object 1: Testing a perfect number (6)
print("--- Object 1: Testing 6 ---")
num1 = Numbers(6)
print(f"Is Prime? {num1.ChkPrime()}")
print(f"Is Perfect? {num1.ChkPerfect()}")
num1.Factors()
print(f"Sum of Factors: {num1.SumFactors()}")
print()

# Object 2: Testing a prime number (11)
print("--- Object 2: Testing 11 ---")
num2 = Numbers(11)
print(f"Is Prime? {num2.ChkPrime()}")
print(f"Is Perfect? {num2.ChkPerfect()}")
num2.Factors()
print(f"Sum of Factors: {num2.SumFactors()}")
print()

# Object 3: Testing a regular composite number (12)
print("--- Object 3: Testing 12 ---")
num3 = Numbers(12)
print(f"Is Prime? {num3.ChkPrime()}")
print(f"Is Perfect? {num3.ChkPerfect()}")
num3.Factors()
print(f"Sum of Factors: {num3.SumFactors()}")