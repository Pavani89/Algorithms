'''
Write a Python function that takes a string as input and returns True if the string is a palindrome
(reads the same forwards and backwards), and False otherwise.
'''

def is_palindrome(string):
#     return string == string[::-1]

    string = string.lower()
    left,right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# Test the function
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False