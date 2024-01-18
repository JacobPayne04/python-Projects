class BankAccount:

    def __init__(self, int_rate=0.01, balance=100): 
        self.balance = balance
        self.int_rate = int_rate


        # deposit function
    def deposit(self, amount):
        self.balance += amount

        # withdraw function
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Tinsufficient funds: charging 5$ overdraft fee")
            self.balance -= 5

        # get balance
    def display_account_info(self):
        print("Balance: ${}".format(self.balance))


        # yeild interest
    def yield_interest(self):
        if self.balance > 0:
            int_earned = self.balance * self.int_rate
            self.balance += int_earned

ba1 = BankAccount()
ba2 = BankAccount()

ba1.deposit(100);ba1.deposit(400);ba1.deposit(500);ba1.withdraw(250);ba1.yield_interest();print(ba1.balance)


ba2.deposit(400);ba2.deposit(789);ba2.withdraw(250);ba2.withdraw(60);ba2.withdraw(46);ba2.withdraw(150);ba2.yield_interest(); print(ba2.balance)


