'''
Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string. solve using regex
'''

import re 

def count_vowels(string):
    string = string.lower()
    pattern = r'[aeiou]'   #pattern = re.compile(r'[aeiou], re.IGNORECASE)
    vowels = re.findall(pattern, string)
    return len(vowels)

# Test the function
string = 'Hello Worldbbhhioiiu'
result = count_vowels(string)
print(result)


'''   W/O the use of regex
def count_vowels(string):
    count = 0
    vowels = "aeiou"
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

# Test the function
print(count_vowels("Hello, World!"))  # Output: 3
print(count_vowels("Python is awesome"))  # Output: 5
''''