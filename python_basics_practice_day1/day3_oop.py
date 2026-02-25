# Task 1 – Create a BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount deposit by {self.account_holder} is {amount}")
       

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Amount withdraw by {self.account_holder} is {amount}")
        else:
            print("Insufficient Balance")
        

    def check_balance(self):
        print(f"Balance left in {self.account_holder} account is {self.balance}")
        

holder_1 = BankAccount("Ritesh", 10000)
holder_1.deposit(2000)
holder_1.withdraw(1000)
holder_1.check_balance()
print("*" * 50)
print("*" * 50)

holder_2 = BankAccount("Ayush", 20000)
holder_2.deposit(5000)
holder_2.withdraw(1000)
holder_2.check_balance()
print("*" * 50)
print("*" * 50)
print("*" * 50)


# Task 2 – Class Variable Experiment
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name
    
    def indentity(self):
        print(f"{self.name}'s object id is {id(self)}")


emp1 = Employee("Ritesh")
emp2 = Employee("Ayush")

print(f"{emp1.name} --> {emp1.company} , {emp2.name} --> {emp2.company}")
print("*" * 50)
print("After changing the class company variable")
print("*" * 50)

Employee.company = "Amazon"

print(f"{emp1.name} --> {emp1.company} , {emp2.name} --> {emp2.company}")
print("*" * 50)
print("After changing the one instance company variable")
print("*" * 50)

emp1.company = "Meta"

print(f"{emp1.name} --> {emp1.company} , {emp2.name} --> {emp2.company}")


# Task 3 – Print id(self)
emp1.indentity()
emp2.indentity()
