"""
File 2 → main.py

Import calculator

Call functions

Add:

if __name__ == "__main__":

Understand deeply:
When you run a file directly vs importing it.
"""

import calculator_module

print("--- Running Main Script ---")
# Access functions using the module name
print("Addition: ",calculator_module.add(10, 10, 10))
print("Subtraction: ",calculator_module.sub(100, 0, 10))
print("Multiplication: ",calculator_module.multi(10, 2, 10))
print("Division: ", calculator_module.divide(0, 10, 10))
print("Division: ", calculator_module.divide(0, 00, 10))