class BankAccount:
    # Class variable
    ROI = 10.5

    def __init__(self, name, amount):
        # Instance variables
        self.name = name
        self.amount = amount

    def display(self):
        """Displays account holder name and current balance."""
        print(f"\nAccount Holder: {self.name}")
        print(f"Current Balance: {self.amount:.2f}")

    def deposit(self, amount):
        """Accepts an amount and adds it to the balance."""
        if amount > 0:
            self.amount += amount
            print(f"Successfully deposited: {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts amount from balance if sufficient funds exist."""
        if amount > self.amount:
            print(f"Insufficient balance! Transaction failed. (Available: {self.amount:.2f})")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.amount -= amount
            print(f"Successfully withdrew: {amount:.2f}")

    def calculate_interest(self):
        """Calculates and returns interest based on ROI."""
        interest = (self.amount * BankAccount.ROI) / 100
        return interest


# --- Demonstration of the Class ---
if __name__ == "__main__":
    print("--- Creating Account 1 ---")
    # Creating first object
    account1 = BankAccount("Piyush Khairnar", 5000.0)
    account1.display()

    # Depositing money
    account1.deposit(2500.0)
    account1.display()

    # Calculating interest
    interest_earned = account1.calculate_interest()
    print(f"Calculated Interest (at {BankAccount.ROI}% ROI): {interest_earned:.2f}")

    # Withdrawing money
    account1.withdraw(3000.0)
    account1.display()

    # Testing insufficient funds
    print("\n--- Testing Insufficient Funds ---")
    account1.withdraw(10000.0)

    print("\n--- Creating Account 2 ---")
    # Creating second object to demonstrate multiple objects
    account2 = BankAccount("Marvellous User", 10000.0)
    account2.display()
    
    interest_earned_2 = account2.calculate_interest()
    print(f"Calculated Interest for Account 2: {interest_earned_2:.2f}")