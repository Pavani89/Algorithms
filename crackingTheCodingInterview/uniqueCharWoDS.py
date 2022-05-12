'''
Given a string, are all the characters unique. What if you cannot use additional data structures
return True or False

Q: If the string is ASCII or a Unicode string.
ASCII - older code. stands for American Standard Code for Information interchange. 128 characters
Unicode - introduced in 1991. simple character set across all platform/language. 2^16 . space efficient
for simplicity let's assume the character set is ASCII

Without Extra Data Structure: We will maintain an integer value called checker (32 bits). As we iterate over the string,
we find the int value of the character with respect to 'a' with the statement int bitAtIndex = str.char(i) - char(a)
Then the bit at that int value is set to 1 with statement 1 <<bitAtIndex
Now, of this bit is already set in the checker, the bit AND operation would make the checker > 0 retun False
Else update checker to make the bit 1 at the index with the statment checker = checker| (1 <<bitAtIndex)

Time Complexity:  O(n)
'''

import math

def uniqueChars(string):
    # assuming string can have characters a-z this has 32 bits set to 0
    checker = 0

    for i in range(len(string)):
        b = string[i]
        c = ord(string[i])
        bitAtIndex = ord(string[i]) - ord('a')

        # If the bit is already set in  checker, return False
        if (bitAtIndex >= 0 ):
            if ((checker & (1 << bitAtIndex)) > 0 ):
                return False

            # Otherwise update and continue by setting that bit in the checker
            checker = checker | (1 << bitAtIndex)

    return True


# Main code
print(uniqueChars('a b cdef jjkw'))
