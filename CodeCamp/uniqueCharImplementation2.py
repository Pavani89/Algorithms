'''
Given a string, are all the characters unique.
return True or False

Q: If the string is ASCII or a Unicode string.
ASCII - older code. stands for American Standard Code for Information interchange. 128 characters
Unicode - introduced in 1991. simple character set across all platform/language. 2^16 . space efficient

for simplicity let's assume the character set is ASCII

Implementation: maintain a boolean array for the character and set a value to True if we encounter in the array.
ASCII has 128 unique characters.

Time Complexity - O(n)
'''

def uniqueChars(string):
    MAX_CHAR = 256

    n = len(string)
    # If length is greater than 256, then some charters must have repeated
    if n > MAX_CHAR:
        return False

    chars = [False] *  MAX_CHAR
    #print(chars)

    for i in range(n):
        index = ord(string[i])
        if (chars[index] == True):
            return False
        chars[index] = True
    return True

print(uniqueChars('a b cdef jjkw'))