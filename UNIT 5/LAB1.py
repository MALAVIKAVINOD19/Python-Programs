class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Input from user
initial_balance = float(input("Enter Initial Balance: "))
account = BankAccount(initial_balance)

deposit_amount = float(input("Enter Amount to Deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter Amount to Withdraw: "))
account.withdraw(withdraw_amount)

account.check_balance()