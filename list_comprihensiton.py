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

#1 Given a list of numbers, remove all odd numbers from the list:

# numbers = [3,5,45,97,32,22,10,19,39,43]
# ruselt = [num for num in numbers if num % 2 == 0]
# print(ruselt)

#2 Given a list of numbers, remove floats (numbers with decimals)
# original_list = [2,3.75,.04,59.354,6,7.7777,8,9]
# ruselt = [i for i in original_list if type(i) == int]
# print(ruselt)

#3 Find all of the numbers from 1-1000 that are divisible by 7
# numbers = int(input('Enter a number'))
# divisiable_of_7 = [num for num in range(numbers) if num % 7 == 0]
# print(divisiable_of_7)

#4 Create a list of all the consonants in the string 
# “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# strings = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
# ruselt = [s for s in strings if s in 'aeiouAEIOU']
# count = len([char for char in strings if char in "aeiouAEIOU"])
# print(ruselt)
# print(count)
########################################## DICTIONARY COMPREHENTIONS ###############################################################



