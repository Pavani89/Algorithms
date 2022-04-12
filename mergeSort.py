'''
Algorithm:
Merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the teo halves, and then merges the two soted halves
1. Divie the lsit recursively into two halves until it can no more be divided
2. merge the smaller lists into new list in sorted order.

time complexity: O(nlogn); best: O(n) - already sorted
space complexity: O(n)
'''


def mergeSort(array):
    pass


# Main
array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
mergeSort(array)

print(" the Sorted array is: ")
for i in range(len(array)):
    print("%d" % array[i], end=" ")

