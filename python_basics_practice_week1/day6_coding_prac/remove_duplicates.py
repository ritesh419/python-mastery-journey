# 🧠 Problem 6 – Remove Duplicates (Preserve Order)

def remove_duplicates(lst):                     # to preserve the order of the list we use, dict.fromkeys() method
    unique_list = list(dict.fromkeys(lst))
    return unique_list

lst = [11, 1, 2, 33, 33, 11, 4, 5, 5]
print(remove_duplicates(lst))