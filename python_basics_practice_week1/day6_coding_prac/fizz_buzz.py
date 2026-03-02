# 🧠 Problem 5 – FizzBuzz

# Print numbers 1 to 50:
# Multiple of 3 → Fizz
# Multiple of 5 → Buzz
# Both → FizzBuzz


for i in range(1, 51):

    if i % 3 == 0 and i % 5 != 0:
        print(f"{i} : FizZ")

    elif i % 5 == 0 and i % 3 != 0:
        print(f"{i} : BuzZ")

    elif i % 5 == 0 and i % 3 == 0:
        print(f"{i} : FizzBuzz")

