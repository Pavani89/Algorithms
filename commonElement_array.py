'''

common elements in two Sorted Arrays
return the common elements as an array between two sorted arrays of integers.

E.g.
array1= [1,3,4,5,7,8,9]
array2 =[1,2,4,6,9,10]
output = [1,4,9]

'''

def common_elements(list1, list2):
    list1_index = list2_index = 0

    result = []   # Final array

    while list1_index < len (list1) and list2_index < len(list2):
        if list1[list1_index] == list2[list2_index]:
            result.append(list1[list1_index])
            list1_index += 1
            list2_index += 2

        elif list1[list1_index] > list2[list2_index]:
            list2_index += 1

        else:
            list1_index += 1
    return result

array1= [1,3,4,5,7,8,9]
array2 =[1,2,4,6,9,10]
print(common_elements(array1, array2))