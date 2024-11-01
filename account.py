from abc import ABC, abstractmethod

# Abstract Base Class for Account
class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance  # Private attribute for encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    @abstractmethod
    def withdraw(self, amount):
        pass  # Abstract method for withdraw

    def get_balance(self):
        return self.__balance

    def _set_balance(self, balance):
        self.__balance = balance  # Encapsulated setter for balance

# SavingsAccount subclass with a withdrawal limit
class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, withdrawal_limit=500):
        super().__init__(account_number, owner, balance)
        self.withdrawal_limit = withdrawal_limit

    # Polymorphic behavior for withdraw method
    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Insufficient funds.")
        elif amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than {self.withdrawal_limit} at a time.")
        else:
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
            print(f"{amount} withdrawn. New balance: {new_balance}")

# CheckingAccount subclass with overdraft functionality
class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=200):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > (self.get_balance() + self.overdraft_limit):
            print("Withdrawal denied. Overdraft limit exceeded.")
        else:
            new_balance = self.get_balance() - amount
            self._set_balance(new_balance)
            print(f"{amount} withdrawn. New balance: {new_balance}")

# System interaction to create accounts and perform transactions
def main():
    print("Welcome to the Banking System")
    
    # Create accounts for demonstration
    saving_acc = SavingsAccount("12345", "Alice", 1000)
    checking_acc = CheckingAccount("67890", "Bob", 500)
    
    # Display initial balances
    print(f"Savings Account Balance: {saving_acc.get_balance()}")
    print(f"Checking Account Balance: {checking_acc.get_balance()}")

    # Perform transactions
    print("\n--- Savings Account Transactions ---")
    saving_acc.deposit(200)
    saving_acc.withdraw(300)
    saving_acc.withdraw(600)  # Exceeds limit, should be denied

    print("\n--- Checking Account Transactions ---")
    checking_acc.deposit(150)
    checking_acc.withdraw(700)  # Within overdraft limit, should succeed
    checking_acc.withdraw(1000)  # Exceeds overdraft, should be denied

if __name__ == "__main__":
    main()
