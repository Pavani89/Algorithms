'''

Problem: Reverse String
Given a string of words, reverse all words

given = "This is the best"
output = "best the is This"
'''

'''
# With python modules
def reverse(s):
    return " ".join(reversed(s.split()))

print(reverse("This is the best"))
'''

'''
# With python modules
def rev(s):
    return s.split()[::-1]

print(rev("This is the best"))
'''

def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    i= 0

    return "".join(reversed(s))

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])

        i += 1

    return "".join(reversed(s))

print(reverse("This is the best"))
