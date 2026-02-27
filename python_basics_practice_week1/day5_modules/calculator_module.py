"""
File 1 → calculator_madule.py

add

subtract

multiply

divide (raise error on zero)
    
"""

def add(*args):
    sums = 0
    for arg in args:
        sums += arg
    return sums

def sub(*args):
    total = args[0]
    for arg in args[1:]:
        total -= arg
    return total

def multi(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(*args):
    try:
        result = args[0]
        for arg in args[1:]:
            if arg== 0:
                raise ZeroDivisionError("Denomenator cannot be 0")
            result /= arg
        return result
    except ZeroDivisionError as e:
        return f"Error occured: {e}"
