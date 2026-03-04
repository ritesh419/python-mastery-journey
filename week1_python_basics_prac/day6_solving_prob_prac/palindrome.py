# 🧠 Problem 2 – Check Palindrome
def is_palindrome_slicing(s):               # slicing method
    clean_str = s.lower().replace(" ","")
    rev_str = clean_str[::-1]
    if rev_str == clean_str:
        return f"Palindrome"
    else:
        return f"Not a paindrome"
    
print(is_palindrome_slicing("Nitin NitiN"))
print(is_palindrome_slicing("step on no pets"))


def is_palindrome_rev_method(s):            # using reversed method
    new_str = s.lower().replace(" ","")
    rev_str = "".join(reversed(new_str))
    if rev_str == new_str:
        return f"Palindrome"
    else:
        return f"Not a paindrome"

print(is_palindrome_rev_method("nitIn"))
print(is_palindrome_slicing("step on no pets"))
print(is_palindrome_slicing("Race Car"))