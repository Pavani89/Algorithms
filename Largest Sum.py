'''

Problem: Largest Sum
Take an array with positive and negative integers and
find the maximum sum of that array
'''

def largestSum(array):
    if len(array) == 0:
        return print('Array too small')

    max_sum = current_sum = array[0]

    for num in array[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max (current_sum, max_sum)

    return max_sum


print(largestSum([7,1,2,-1,3,4,10,-12,3,21,-19]))