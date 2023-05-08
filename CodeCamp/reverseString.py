"""
	Given a string, reverse the words
"""

def reverse_string(text):
	wordList = text.split()
	reverseWordList = wordList[::-1]
	return ' '.join(reverseWordList)
	

print(reverse_string('I am Home'))
print(reverse_string('We are Ready'))