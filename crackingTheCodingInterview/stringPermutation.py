'''
Given two strings write a method to decide if one is a permutation of the other

confirm the details from the interviewer:
is the permutation case sensitive?
whitespaces?

Brute solution:
1. Sort the two string
2. compare them
Time Complexity: O(n^2)

optimised solution:
Assumption: set of possible characters in both strings is small,
it is assumed that the characters are stored using 8 bit and there can be 256 possible characters.
1) Create one count array of size 256 for both strings. Initialize all values in count arrays as 0.
2) Iterate through every character of first string and increment the count of character
3) Iterate through every character of second string and decrement for characters
4) If the count of the final is zero then return True. Ele False
Time Complexity: O(n)
'''

NO_OF_CHARS = 256

def arePermutation(str1, str2):
    # remove spaces and lower
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the two strings are of same length
    if len(str1) != len(str2):
        return False

    # Create a counter and set all the values to 0
    count = [0 for i in range(NO_OF_CHARS)]
    i = 0

    # Iterate and operate the counter
    for i in range(len(str1)):
        count[ord(str1[i])] += 1
        count[ord(str2[i])] -= 1

    # check if the counter has value
    for i in range(NO_OF_CHARS):
       if count[i] > 0 :
           return False
    return True

# Main
str1 = "aAbbccdd"
str2 = "ddc cbbaa"

print(arePermutation(str1, str2))