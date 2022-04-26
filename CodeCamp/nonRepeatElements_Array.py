"""
Non repeat element

Take a string and return character that never repeat
if multiple uniques then return only the first unique

"""

def non_repeating(string):
    string = string.replace(' ', '').lower()
# remove .lower if looking for unique charter and not alphabet

    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

#solution for if multiple uniques then return only the first unique
#    for char in string:
#        if char_count[char] == 1:
#            return char

#    return None

#if multiple  print all the unique chars

    all_uniques = []
    # sort the dictionary so that the values control the order (ascending order)
    y = sorted(char_count.items(), key=lambda x: x[1])
    #print(y)

    for item in y:
        if item[1]  == y[0][1]:
            all_uniques.append(item)
    return all_uniques

print(non_repeating('I Apple peels Ape'))