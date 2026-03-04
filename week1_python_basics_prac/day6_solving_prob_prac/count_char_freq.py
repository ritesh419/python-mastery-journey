# 🧠 Problem 3 – Count Character Frequency
def char_frequency(s):                      # simple logic 
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

def char_freq(s):                           # using get method >> dict.get(key, default)
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("apple"))
print(char_freq("apple"))