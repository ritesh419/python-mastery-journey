# 🧩 Problem 1 – Reverse Array (Without slicing)
def rev_array(new_list):
    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - i - 1):
            new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
    return new_list


# new_list = [1, 2, 5, 3, 4, 10, 11]
# print(rev_array(new_list))


# 🧩 Problem 2 – Find Second Largest (Without sorting)
def sec_largest(new_list):
    max_val = float("-inf")
    for i in new_list:
        if i > max_val:
            max_val = i
    new_list = [j for j in new_list if j != max_val]
    max_val = float("-inf")
    for k in new_list:
        if k > max_val:
            max_val = k
    return max_val


# new_list = [1, 12, 3, 14, 15, 15]
# print(sec_largest(new_list))


# 🧩 Problem 3 – Remove Duplicates (Return new list)
def rem_dupl(new_list):
    unique_list = []
    for item in new_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# new_list = [1,1,1,3,3,4,5]
# print(rem_dupl(new_list))


# 🧩 Problem 4 – Move All Zeros To End
def non_zero_collector(new_list):
    placement = 0
    for explorer in range(len(new_list)):
        if new_list[explorer] != 0:
            new_list[explorer] , new_list[placement] = new_list[placement] , new_list[explorer]
            placement += 1
    return new_list

new_list = [0, 1, 0, 3, 12]
print(non_zero_collector(new_list))