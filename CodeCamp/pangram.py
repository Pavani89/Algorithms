"""
	Given a string, whether the string is pangram or not
	pangram - containing every letter of the alphabet at least once.
"""
import string

def pangram_string(text, alphabet=string.ascii_lowercase):
	# create a set of alphabets
	alphaset = set(alphabet)

	# remove any spaces form the input string
	text = text.replace(" ", "" )

	# convert the string to all lower case
	text = text.lower()

	# grab all unique letters from the string using set()
	text = set(text)

	# check if alphabet set == string set() from input
	return text == alphaset

print(pangram_string('The quick brown fox jumps over the lazy dog'))
print(pangram_string('We are Ready Ready Ready Ready Ready Ready Ready'))