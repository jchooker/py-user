class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Account balance for {self.name}: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

testUser1 = User("Joseph Hooker", "jcoleh@yahoo.net")
testUser2 = User("Emily Hooker", "ewarnahooker@ualr.biz")
testUser3 = User("Nutler Hooker", "smalldaddi@pawspace.pizza")

testUser1.make_deposit(300).make_deposit(1200).make_deposit(250).make_withdrawal(600).display_user_balance()