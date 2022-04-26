'''
Problem statement:
Given two strings, check to see if they are anagrams.
eg:
"client eastwood" is an anagram of "old west action"
'''

'''
Solution 1: Using Python modaules

def anagram(s1, s2):
  #remove spaces and lower
  s1= s1.replace(" ", "").lower()
  s2= s2.replace(" ", "").lower()

  # return boolean for sorted match
  return sorted(s1)== sorted(s2)
anagram('dog','god')
'''


# solution 2:

def anagram(s1, s2):
    # remove spaces and lower
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # check if the same number of letters
    if len(s1) != len(s2):
        return False

    # count the frequency of each letter
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1  # add 1 to the letter if it exits in the dictionary
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1  # add 1 to the letter if it exits in the dictionary
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

        return True


x = anagram('god', 'dog')
print(x)
