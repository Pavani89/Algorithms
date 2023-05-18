'''
Challenge: Merge Sorted Lists
Write a Python function that takes two sorted lists as input and returns a new sorted list that contains all the elements from both lists.
'''

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Append remaining elements
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Test the function
print(merge_sorted_lists( [2, 4, 6], [1, 3, 5]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([10, 20, 30], [5, 15, 25]))  # Output: [5, 10, 15, 20, 25, 30]
print(merge_sorted_lists([10, 20, 30], [5, 15, 25, 35]))  # Output: [5, 10, 15, 20, 25, 30, 35]
