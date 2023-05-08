"""
	Return the sum of the numbers in the array, except ignore sections of numbers strating with a 6 and extending to 
	the next 9. Return 0 for no numbers (ecery 6 will be followed by atleast one 9)
"""

def summer_69(nums):
	total = 0
	add = True

	for num in nums:
		while add:
			if num != 6:
				total += num
				break
			else:
				add = False

		while not add:
			if num != 9:
				break
			else:
				add = True
				break
		
	return total




print(summer_69([1,3,5]))   // 9
print(summer_69([6,3,9]))	// 0
print(summer_69([1,6,9]))	// 1
print(summer_69([]))		// 0
print(summer_69([9, 1, 6, 2, 9, 9]))	//19