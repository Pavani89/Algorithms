'''
pseudocode:
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration. Insertion sort works similarly as we sort cards in our hand in a card game.
1. The first element in the array is assumed to be sorted. Take the second element and store it separately in key. Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.
2. The first two elements are now sorted. Take the third element and compare it with the elements on the left of it. Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.
3. Similarly, place every unsorted element at its correct position

time complexity: O(n^2); best: O(n) - already sorted
space complexity: O(1) ; because an extra variable key is used.

The insertion sort is used when:
1.The array is has a small number of elements
2. There are only a few elements left to be sorted
'''


def insertionSort(array):
    pass


# Main
array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
insertionSort(array)

print(" the Sorted array is: ")
for i in range(len(array)):
    print("%d" % array[i], end=" ")
