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

#solution 2:

def anagram(s1, s2):
  #remove spaces and lower
  s1= s1.replace(" ", "").lower()
  s2= s2.replace(" ", "").lower()
  
  
