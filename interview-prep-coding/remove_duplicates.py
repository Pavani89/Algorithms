'''
Write a Python function that takes a list as input and returns a new list with duplicate elements removed, while preserving the original order of elements.
'''

def remove_duplicates(lst):
    # return list(dict.fromkeys(lst))
    return list(set(lst))

# Test the function
lst = [1, 2, 3, 3, 4, 2, 5]
result = remove_duplicates(lst)
print(result)  # Output: [1, 2, 3, 4, 5]
