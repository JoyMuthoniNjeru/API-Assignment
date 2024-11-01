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
