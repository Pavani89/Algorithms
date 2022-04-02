'''
pseudocode:
1. Let min = 0 and max = n-1.
2. Compare x with the middle element.mid is the average if min and max
3. If x matches with the middle element, we return the mid index.
4. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half. with mim = mid +1
5. Else (x is smaller) recur for the left half.
6. repeat step 2

time complexity: O(log n)
space complexity: O(1) ; we only need two variable to keep track of the range of elements that are to be checked.
'''

'''
#Below is recursive implementation of Binary search

def binarySearch(array, min, max, x):
    # Set the base case
    if max >= min:

        mid = ( min + max ) // 2

        # If element is present at the middle itself
        if array[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > x:
            return binarySearch(array, min, mid -1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(array, mid + 1, max, x)

    else:
        # Element is not present in the array
        return -1

# Main
array = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(array, 0, len(array) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")        
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

        # If x is greater, ignore left half
        if array[mid] < x:
            min = mid + 1

        # If x is smaller, ignore right half
        elif array[mid] > x:
            max = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
array = [2, 3, 4, 10, 40]
x = 1000

# Function call
result = binary_search(array, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")





