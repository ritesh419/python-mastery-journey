# 🧩 Problem 1 – Count Character Frequency
def count_char(ch):
    freq_dict = {}
    for item in ch:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

# print(count_char("appoleee"))

# 🧩 Problem 2 – First Non-Repeating Character
def non_repeating_char(ch):
    freq_dict = count_char(ch)
    for ki in freq_dict:
        if freq_dict[ki] == 1:
            return ki
    else:
        return None

# print(non_repeating_char("aappllle"))



# 🧩 Problem 3 – Check Anagram

# not a good way to solve the problem, it has a lot of issue, like time complexity, edge cases, DRY rule.
def check_anagram(letter_one, letter_two):
    if len(letter_one) == len(letter_two):
        chars_one = list(letter_one)
        chars_two = list(letter_two)
        #sort both the array
        for i in range(len(chars_one)-1):
            for j  in range(len(chars_one)-i-1):
                if chars_one[j] > chars_one[j+1]:
                    chars_one[j], chars_one[j+1] = chars_one[j+1], chars_one[j]
        for i in range(len(chars_two)-1):
            for j  in range(len(chars_two)-i-1):
                if chars_two[j] > chars_two[j+1]:
                    chars_two[j], chars_two[j+1] = chars_two[j+1], chars_two[j]
        if chars_one == chars_two:
            print("It is a Anagram")
        else:
            print("Length is equal but not a Anagram")
    else:
        print("Not a Anagram")

# check_anagram("listen", "silent")


# using dictionary to solve the problem now, it is handling edge cases, time complexity-> O(n) instead of above O(n^2) and also we are reusing our code here.
def anagram_check(ltr_one, ltr_two):
    fre_dict1 = count_char(ltr_one.lower().replace(" ", ""))
    fre_dict2 = count_char(ltr_two.lower().replace(" ", ""))
    return fre_dict1 == fre_dict2
# print(anagram_check("lisTen", "S ilent"))
    

# 🧩 Problem 4 – Longest Word in Sentence
def long_word(sentence):
    long_list = sentence.split()
    longest = ""
    for i in long_list:
        clean_word = i.strip(",.!")
        if len(clean_word) > len(longest):
            longest = clean_word
    print(longest)

long_word("I am Ritesh, who lives in India")