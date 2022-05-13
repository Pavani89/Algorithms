'''

Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word that is same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need
to be limited to just dictionary words.

Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc)

Assumption:
ASCII characters.
0. remove spaces, make the charaterset all lowercase
1. Check if the length of the input is  >1. If one, return True
2. create a counter array for the characters
3. As you run through the string, increment the count for the character as you encounter
4. iterate through the counter, check if the value is divisible by 2
5. for the single character, keep another counter, if this counter exceeds 2 then return false.

Time Complexity: O(n)
'''

# Character set in ASCII
MAX = 256

def palinPermute(string):
    string = string.replace(" ", "").lower()

    if len(string) == 1:
        return True

    counter = [0 for i in range(MAX)]
    onesie = 0

    for char in string:
        counter[ord(char)] += 1

    for i in range(len(counter)):
        if counter[i] % 2 != 0:
            onesie += 1
        #i += 1

    if onesie > 1:
        return False
    return True


# Main code
# input = "geeksogeeks"
input = "geeksforgeeks"
output = palinPermute(input)
print(output)
