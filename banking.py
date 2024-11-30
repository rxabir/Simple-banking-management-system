class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            #self.balance = self.balance + amount
            return  amount
        else:
            return f"Amount less than 0 can't be deposited"

    def Check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            #self.balance = self.balance - amount
            self.balance -= amount
            return amount
        else:
            return f"Insufficient balance"



obj = Banking("Abir",10000)
print(f"Account name: {obj.name}")
print(f"Initial Balance is: {obj.balance}")
print(f"Deposite Balance: {obj.deposit(5)}")
print(f"After Deposite, Your balance is : {obj.Check_balance()}")
print(f"Withdraw Balance: {obj.withdraw(2000)}")
print(f"After Withdraw, Your balance is: {obj.Check_balance()}")