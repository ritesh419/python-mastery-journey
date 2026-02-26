# Task 1 – Inheritance Practice
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print("Parent constructor called")

    def ride(self):
        print("Driving any vehicle")


class Car(Vehicle):
    def __init__(self, brand, model):  
        super().__init__(brand) #accessing parent variable in child class using super()
        self.model = model

    def ride(self):             #method overriding
        print("Driving a car")
        super().ride()          #accessing parent method in child class using super()

# Task 2 – Use super()

# obj = Car("BMW", "M5")
# obj.ride()


# Task 3 – Encapsulation

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance       # private attribute

    def deposit(self, amount):
        self.__balance += amount 
        print("Amount deposit, now balance is: ", self.__balance)

    def withdraw(self):
        print("Amount withdraw")

    def get_balance(self):
        print("Balance in the Account", self.__balance)

# obj1 = BankAccount(1000)
# obj1.deposit(100)
# # print(obj1.__balance)   # Throws an error >> AttributeError

# obj1.get_balance()  # right way to access the private attribute
# print(obj1._BankAccount__balance)       # alternate way to access the private attribute


# Task 4 – Dunder Method

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        # User-friendly: Designed for the end user
        return f"{self.name} has bought car in ${self.price}"
    
    def __repr__(self):
        # Developer-friendly: Formal representation to recreate the object
        return f"'{self.name}' | {self.price}"

obj2 = Product("Ritesh", 50000)
print(str(obj2))
print(obj2.__repr__())

print(obj2)                     # Default print() uses __str__