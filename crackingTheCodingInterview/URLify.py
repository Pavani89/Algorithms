'''
Write a method to replace all spaces with '%20'. You may only assume that the string
has sufficient space at the end to hold additional characters, and that you are given the
"true" length of the string

input: "Mr John Smith    ",13
Output: "Mr%20John%20Smith"

pseudo code:
brute force - Use python library to strip extra spaces and replace spaces with %20
def URLify(str, length):
    str = str.strip()
    str = str.replace(input[i], '%20')
    return str

better solution is to perform inplace replacement -
The algorithm employs a two-scan approach. In the first scan,
we count the number of spaces. By tripling this number, we can compute how many extra charaters we
will have in the final string.
In the second pass, which is done in the reverse order, we actually edit the string.
When we see space, we replace it with %20. If no space, copy the original character.

Time complexity: O(n)
'''
# Maximum length of string after modifications.
MAX = 1000

# Replace spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]
def replaceSpaces(string):
    # Remove leading and trailing spaces
    string = string.strip()

    i = len(string)

    # count spaces and find current length
    space_count = string.count(' ')

    # Find new length.
    new_length = i + space_count * 2

    # New length must be smaller than length
    # of string provided.
    if new_length > MAX:
        return -1

    # Start filling character from end
    index = new_length - 1

    string = list(string)

    # Fill string array
    for f in range(i - 2, new_length - 2):
        string.append('0')

    # Fill rest of the string from end
    for j in range(i - 1, 0, -1):

        # inserts %20 in place of space
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1

    return ''.join(string)


# Driver Code
if __name__ == '__main__':
    s = "Mr John Smith "
    s = replaceSpaces(s)
    print(s)
