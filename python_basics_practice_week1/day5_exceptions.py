"""
Task 1 >>
Write a program that:
Takes integer input
Handles ValueError
Handles ZeroDivisionError
"""

try:
    user = input("Enter the two numbers to divide keep space in between: ").split()
    num1 = int(user[0])
    num2 = int(user[1])
    operation = num1/num2
except ValueError:
    print("Error: Please enter a number")
except ZeroDivisionError:
    print("Error: Number cannot be divided by Zero")
except Exception as e:
    print("An unexpected error occured ", e)
else:
    print("The result is ",operation)
finally:
    print("Thank you!")


"""
Task 2 >>
Write function:
def divide(a, b):
Raise ValueError if b == 0
Handle it using try/except
"""

def divide(a, b):
    try:
        if b == 0:
            raise ValueError("b value cannot be 0")
        print(a/b)
    except ValueError as e:
        print(f"Caught an Error: {e}")
    
obj = divide(10, 0)
    

"""
Task 3
Create custom exception:
class InvalidAgeError(Exception):
    pass
Write function that:
Raises error if age < 18
"""

class InvalidAgeError(Exception):
    pass

def driving_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age is under 18 - not eligible for driving")
    except InvalidAgeError as e:
        print(f"Error caught: {e}")
    else:
        print("Eligible for driving")

obj2 = driving_age(18)