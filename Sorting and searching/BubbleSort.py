'''
pseudocode:
1. Bubble sort is the simplest sort algorithm that works repeated swapping adjacent elements if they are in wrong order
2. In first cycle, Start by comparing 1st and 2nd element and swap if 1st element is greater.
3. After that do the same for 2nd and 3rd element.At the end of cycle you will get max element at the end of list.
4. Repeat step 2 and 3 for (number of elements – 1) times to get the sorted list.

time complexity: O(n^2); best: O(n) - already sorted
space complexity: O(1) ; inplace swapping,so no additional memory
'''


def bubbleSort(array):
    n = len(array)

    # Outer loop to traverse through all the elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # print(i, j)
            # swap if the element found is greater than the next
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # If no swapping is needed at the end of first traversal, break.
        if not swapped:
            break


# Main
# array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
array = [1, 2, 4]
bubbleSort(array)

print(" the Sorted array is: ")
for i in range(len(array)):
    print("%d" % array[i], end=" ")
