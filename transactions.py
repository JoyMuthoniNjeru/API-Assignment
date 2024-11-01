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
