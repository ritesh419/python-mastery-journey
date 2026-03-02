# 🧠 Problem 4 – Find Second Largest Number

# def second_largest(nums):                       # logic-wise right
#     largest_num = float('-inf')
#     sec_lar_num = float('-inf')
#     new_set = set(nums)
#     nums = list(new_set)

#     print(type(nums))
#     print(nums)

#     for i in range(len(nums)):
#         if nums[i] > largest_num:
#             largest_num = nums[i]

#     nums.remove(largest_num)
#     print(nums)

#     for i in range(len(nums)):
#         if nums[i] > sec_lar_num:
#             sec_lar_num = nums[i]

#     return sec_lar_num


# nums= [-1, -20, -30, -10, -11]
# print(second_largest(nums))




# def second_largest_num(nums):                       # cleaner code
#     largest = float('-inf')
#     second = float('-inf')

#     for num in nums:

#         if num > largest:
#             second =  largest
#             largest = num

#         elif num > second and num != largest:
#             second =  num

#     if second == float('-inf'):
#         return "No second largest element"
    
#     return second


# nums= [1, 20, 20, 10, 11]
# print(second_largest_num(nums))



def sec_lar_num(nums):                          # using sort() method, more pythonic way
    unique_list = list(set(nums))

    if len(unique_list) < 2:
        return "No second largest element"
    
    unique_list.sort()
    return unique_list[-2]


nums= [1, 20, 20, 10, 11]
print(sec_lar_num(nums))
