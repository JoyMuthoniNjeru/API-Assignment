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
