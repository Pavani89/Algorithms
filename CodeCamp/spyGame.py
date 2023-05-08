"""
	Given a list of ints, return True if it contains 007 in order
"""

def spy_game(nums):
	# create a template of  0 0 7, list
	# pop(0) with each match.
	# at the end, if code is 1, return True

	code = [0, 0, 7, 'x']
	for num in nums:
		if num == code[0]:
			code.pop(0)

	return len(code) == 1


print(spy_game([1,3,1,3, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 4, 0, 5]))