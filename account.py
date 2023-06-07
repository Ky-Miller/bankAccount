class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance=0): 
        self.int_rate = int_rate * balance
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print('INSUFFICIENT FUNDS: Charging a $5 fee')
        return self
    def display_account_info(self):
        print("Balance:" + " $" + str(self.balance))
        return self
    def yield_interest(self):
        self.balance += self.int_rate
        return self
    @classmethod
    def display_accounts(cls):
        print (cls.accounts)
User_1 = BankAccount(int_rate=0.015, balance=200)
User_1.deposit(50).deposit(500).deposit(650).withdraw(1250).yield_interest().display_account_info()

User_2 = BankAccount(int_rate=0.01, balance=12)
User_2.deposit(500).deposit(30).withdraw(15).withdraw(26).withdraw(41).withdraw(650).yield_interest().display_account_info
BankAccount.display_accounts()