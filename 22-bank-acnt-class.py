"""
Bank Account Class
Features:
Deposit
Withdraw
Check Balance
"""

class bank_accnt:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance+=amount
        print("Money deposited successfully\n")
    def withdraw(self, amount):
        if self.balance>=1000 and self.balance-amount>=1000:
            self.balance-=amount
            print("Money withdrawn successfully\n")
        else:
            print("Do not have sufficient balance\n")
    def check_balance(self):
        print("Your account Balance: ", self.balance)
        print()

in_bal = int(input("enter initial balance: "))
account = bank_accnt(in_bal)
while True: 
    options = int(input("press 1 to deposit, 2 to withdraw, 3 to check balance, 4 to exit: "))
    if options == 1:
        principal=int(input("enter the money to deposit: "))
        account.deposit(principal)
    elif options == 2:
        w_amt=int(input("enter the money to withdraw: "))
        account.withdraw(w_amt)
    elif options == 3: 
        account.check_balance()
    elif options == 4:
        print("Exited successfully\n")
        break
    else:
        print("Invalid option. Try again\n")
