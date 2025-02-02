class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance (default is 0)."""
        self.__account_balance = initial_balance  # Encapsulation (private attribute)

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    