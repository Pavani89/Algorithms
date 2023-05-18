'''
Challenge: Find Common Elements
Write a Python function that takes two lists as input and returns a new list that contains the common elements between the two lists.
'''

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements

# Test the function
print(find_common_elements([1, 2, 3, 4, 5], [4, 5, 6,7]))