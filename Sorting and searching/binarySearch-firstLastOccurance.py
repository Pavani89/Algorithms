# Find first and last occurrences of a number in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1

# leftBias = [True/False], if false, result is rightBiased
def binSearch(nums, target, leftBias):
    left, right = 0, len(nums) -1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            index = mid
            if leftBias:
                right = mid - 1
            else:
                left = mid + 1
    return index

nums = [2, 6, 7, 8, 8, 10]
target = 10
leftIndex = binSearch(nums, target, True)
rightIndex = binSearch(nums, target, False)
print(leftIndex, rightIndex)