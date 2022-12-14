#How to sort elements of a tuple?
# Python tuples do not have the sort method. So, to sort the elements of a tuple, the sorted 
# builtin function can be used by passing the tuple as the argument. The function returns a list with the items 
# of tuple sorted in ascending order. This list can be converted into a tuple by using tuple( ).
#  The default sorting order is ascending order.

# tup_raw = (7, 2, 5, 4)
# result = sorted(tup_raw)
# tup_sorted = tuple(result)
# print('Sorted Tuple :', tup_sorted)
####################################################################################
# How to delete a tuple?
# del.my_tuple would delete my_tuple

# How to add an element to a tuple?
# Since tuples are immutable, elements cannot be added/modified/deleted from a tuple.

# How to find the index of specific element in a tuple?
# my_tuple.index(element,start,end) would retun the position of the first occurrence of the
#  element in the tuple and If the element is not found, ValueError is raised.

###############################################################################################
# Can a tuple be a member in another tuple?
# Yes, tuples can be nested to any depth needed.
# tup1 = (1, 2, 3)
# tup2 = ('gk', 'nxt')
# nested_tuple = (tup1, tup2)
########################################################################################
