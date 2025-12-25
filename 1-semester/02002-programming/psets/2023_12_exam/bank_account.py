class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount

    def withdraw(self, amount):
        self.amount = amount
        if (self.balance - self.amount) < 0: return 0
        else:
            self.balance -= self.amount
            return self.amount

    def get_balance(self):
        return self.balance 
    
class OverdraftAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        self.amount = amount
        if (self.balance - self.amount) >= -self.overdraft_limit:
            self.balance -= self.amount
            return self.amount
        else:
            return 0