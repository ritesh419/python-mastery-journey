# 🧠 Problem 7 – Anagram Check
"""

An anagram example is rearranging the letters of "listen" to form "silent," or "heart" to make "earth," demonstrating how the same letters create new words, like "gum" and "mug," or phrases like "debit card" and "bad credit". Anagrams use all the original letters exactly once to form a different word or phrase. 

"""

def is_anagram(s1, s2):              
    lst1 = {}
    lst2 = {}
    if len(s1) == len(s2):
        for char1 in s1:
            lst1[char1] = lst1.get(char1, 0) + 1        # using dict.get(key, default) method for char freq
        
        for char2 in s2:
            lst2[char2] = lst2.get(char2, 0) + 1

        if lst1 == lst2:
            return "It is a anagram"
        else:
            return "length is equal but not a anagram, as letters are not same in both"
    else:
        return "Not a anagram"
    
s1 = "listed"
s2 = "silent"
print(is_anagram(s1, s2))