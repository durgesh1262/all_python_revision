# list1 = [5,223,55,77,44,88,11,22,35,56,88]
# mylist = [i for i in list1 if i%2==0]
# print(mylist)

# using join() and split()

# s = 'canopus is a grate company'
# result = s.split(' ')
# print(result)

# re_result = ' '.join(result)
# print(re_result)
#################################################################################################
# What is list comprehension?
# The list comprehension syntax is somewhat of a compressed ‘for’ loop.

#Given a list of numbers, remove all odd numbers from the list:

numbers = [3,5,45,97,32,22,10,19,39,43]
ruselt = [num for num in numbers if num % 2 == 0]
print(ruselt)