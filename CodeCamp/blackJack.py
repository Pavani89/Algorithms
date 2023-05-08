"""
Given 3 integers between 1 and 11, if their sum is less or equal to 21, return sum.
if sum exceeds 21 and there's an 11, reduce the total sum by 10.
if the sum still exceeds return 'BUST'
"""

def black_jack(a, b, c):
	if sum([a,b,c]) <= 21:
		return sum([a,b,c])
	elif 11 in [a, b, c] and sum([a,b,c]) <=31:
		return sum([a,b,c]) - 10
	else:
		return "BUST"

print (black_jack(5,6,7))
print (black_jack(1,3,3))
print (black_jack(11,9,9))
print (black_jack(19,9,9))