from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
def make_deposit(self, amount):
    self.account.make_deposit(amount)
    return self

def make_withdrawl(self,amount):
    self.account.make_withdrawl(amount)
    return self