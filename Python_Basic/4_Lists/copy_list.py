import copy

list_val = [1,2,3,4,5,6]
list_list = [list_val, ['Sun', 'Moon', 'Stars']]

# Copying references
list_copy = list_val
list_copy[3] = 'Alice'
print(list_val, list_copy)

# copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary
list_copy_1 = copy.copy(list_val)
list_copy_1[0] = 'Leo'
print(list_copy_1, list_copy, list_val)

# If the list you need to copy contains lists, then use the copy.deepcopy() function
print('List of list:', list_list)
list_deep_list = copy.deepcopy(list_list)
list_deep_list[1][0] = 'Mercury'
print('List of list after modification: ', list_deep_list, list_list)