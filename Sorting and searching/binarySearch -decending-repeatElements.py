'''

array = [8, 6, 5, 3, 2, 1]
x = 1
pseudocode:
1. Let min = 0 and max = n-1.
2. Compare x with the middle element.mid is the average if min and max
3. If x matches with the middle element, we return the mid index.
4. Else If x is lesser than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half. with mim = mid +1
5. Else (x is larger) check for the left half.
6. repeat step 2

time complexity: O(log n)
space complexity: O(1) ; we only need two variable to keep track of the range of elements that are to be checked.
'''

'''
#Below is iterative implementation of Binary search
'''


def binary_search(array, x):
    min = 0
    max = len(array) - 1
    mid = 0

    while min <= max:
        mid = (min + max) // 2

        # If x is lesser, ignore left half
        if array[mid] > x:
            min = mid + 1
        # If x is bigger, ignore right half
        elif array[mid] < x:
            max = mid - 1
        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
array = [8, 6, 4, 3, 2, 1, 1]
x = 1

# Function call
result = binary_search(array, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")