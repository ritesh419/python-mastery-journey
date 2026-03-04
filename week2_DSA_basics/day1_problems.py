# 🧩 Problem 1 – Find Maximum Element
def max_element(new_list):
    maximum_element = float('-inf')
    for i in new_list:
        if i > maximum_element:
            maximum_element = i
    return maximum_element
    
# new_list=[-10, 12, 1, -324, 3]
# print(max_element(new_list))


# 🧩 Problem 2 – Find Minimum Element
def min_element(new_list):
    minimum_element = float('inf')
    for i in new_list:
        if i < minimum_element:
            minimum_element = i
    return minimum_element

# new_list=[-10, 12, 1, -4, 3]
# print(min_element(new_list))


# 🧩 Problem 3 – Sum of All Elements
def sum_element(new_list):
    total = 0
    for i in new_list:
        total += i
    return total

# new_list=[-10, 12, 1, -4, 3]
# print(sum_element(new_list))


# 🧩 Problem 4 – Check If Array Is Sorted
def sorted_array(new_list):
    for i in range(len(new_list)-1):
        if new_list[i] <= new_list[i+1]:
            continue
        else:
            return "Array is not sorted"
    return "Array is sorted"

# new_list=[-10, 1, 1, 2, 3, 2]
# print(sorted_array(new_list))


