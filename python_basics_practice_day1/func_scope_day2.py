# Task 1 – Custom Calculator
def custom_calculator(op, *args):
    if op == "add":
        return sum(args)
    else:
        multi = 1
        for arg in args:
            multi = arg * multi
        return multi

inp_operation_num = input("Enter whether you want to multiply or add the numbers: ")
inp_nums = input("Enter the numbers: ").split()
nums = map(float, inp_nums)
print(custom_calculator(inp_operation_num, *nums))

# Task 2 – User Profile Builder
def create_user(name, age, **kwargs):
    profile = {
        "name": name,
        "age": age
    }
    profile.update(kwargs)
    return profile

# name = "Ritesh"
# age = 22
# user = {"id": 1, "email": "abc@gmail.com"}
# print(create_user(name, age, **user))


# Task 3 – Scope Experiment
name = "Ayush"

def naming():
    name ="Ritesh garkoti"
    print("Inside local var: ", name) 

print("before naming global: ", name)
naming()
print("after naming global: ", name)

def user_naming():
    global name 
    name = "Ayush Garkoti"
    print("Inside user_naming function: ",name)

user_naming()
print("Global now changed: ", name)

def outer_fun():
    name = "Synix"
    def inner_fun():
        nonlocal name 
        name = "Syniii"
        print("Inside inner func: ", name)
    inner_fun()
    print("Inside outer fun: ", name)

outer_fun()
print("name in global: ", name)