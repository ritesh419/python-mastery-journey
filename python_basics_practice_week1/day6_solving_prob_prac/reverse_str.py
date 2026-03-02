# 🧠 Problem 1 – Reverse a String (No slicing)
def reverse_string(s):      # building new str
    emp_str = "" 
    for char in s:
        emp_str = char + emp_str
    return emp_str

def rev_str_list(s):        # using indexed loop  
    emp_str = ""
    for i in range(len(s)-1, -1, -1):
        emp_str += s[i]
    return emp_str

print(reverse_string("ritesh"))
print(rev_str_list("ayush"))
