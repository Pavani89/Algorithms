'''
given a string = 'aabbbcddddacd' write a python program to output the character and the number of times  as a dictionary
'''

def count_characters(string):
    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

# Test the function
# string ='aabbccdddddddabcd'
string = 'aabbbcddddacd'
result = count_characters(string)
print(result)

'''
same solution but using regex

import re

def count_consecutive(string):
    pattern = r'(.)\1*'      #'(.)\1*' to match consecutive occurrences of any character.
    matches = re.findall(pattern, string)
    char_counts = {match[0]: len(match) for match in matches}
    return char_counts

# Test the function
string = 'aabbbcddddacd'
result = count_consecutive(string)
print(result)
'''