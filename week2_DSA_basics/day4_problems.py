"""
Two Pointer Technique
Used for:
>> array reversal
>> pair sum
>> palindrome check
>> removing duplicates
"""

# 🧩 Problem 1 – Palindrome String
def check_palindrome(st):

    # st_list = list(st)        # works extra like doing extra checks and reversing whole string
    # left = 0
    # right = len(st_list) - 1
    # while left < right: 
    #     st_list[left], st_list[right] = st_list[right], st_list[left]
    #     left += 1
    #     right -= 1
    # palindrome_st = ''.join(st_list)
    # if st == palindrome_st:
    #     return True
    # else:
    #     return False

    n = len(st)             # optimal as it is just checking every str item one by one and also works half then before
    for i in range(n // 2):
        if st[i] != st[n-i-1]:
            return False
    return True

# print(check_palindrome("!racecar!"))


# 🧩 Problem 2 – Two Sum (Pair Sum)
def two_sum(arr, target):
    # n = len(arr)            # TC -> O(n^2)
    # for i in range(n-1):
    #     if arr[i] + arr[i+1] == target:
    #         return True
    # else:
    #     return False

    seen = set()        # TC-> O(n) , Hasp map is used
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)

    return False
    
arr = [2, 7, 11, 15]
print(two_sum(arr, 13))


# 🧩 Problem 3 – Remove Duplicates From Sorted Array
def remove_duplicate(arr):

    # unique_arr = []       # TC -> O(n^2)
    # for i in arr:
    #     if i not in unique_arr:
    #         unique_arr.append(i)
    # return unique_arr

    if not arr:
        return []
    result = [arr[0]]       # TC-> O(n)
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result

# arr = [11, 11, 11, 2, 23, 23]
# print(remove_duplicate(arr))


# 🧩 Problem 4 – Valid Palindrome Sentence
def valid_palindrome_sent(sent):
    clean_sent = "".join(c.lower() for c in sent if c.isalnum())
    n = len(clean_sent)
    for i in range(n//2):
        if clean_sent[i] != clean_sent[n-i-1]:
            return False
    return True

# print(valid_palindrome_sent("A man a plan a canal Panama"))