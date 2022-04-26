'''
Given a string, are all the characters unique.
return True or False

'''

'''
Using python in built modules
def uniqueChars(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)
'''

def uniqueChars(string):
    string = string.replace(' ', '')
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True


print(uniqueChars('a b cdef jjkw'))