#  list with uinig in oprator
# mylist = [1,2,3,4,5,6,'a','d','#']
# result = 'a' in mylist
# print(result)
###################################################################################
# 2. How to iterate over 2+ lists at the same time
# You can zip() lists and then iterate over the zip object.
#  A zip object is an iterator of tuples.

# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]

# z  = zip(name,animal,age)

# for name,animal,age in z:
#     print('{} the {} is age {} '.format(name,animal,age))
#########################################################################################
#6. What is the difference between append and extend?
#.append() adds an(only one) object to the end of a list.

# a = [1,2,3]
# a.append(4)
# print(a)

# a.append([5,6])
# a #=> [1, 2, 3, 4, [5, 6]]

# .extend() .extend() adds each value from a 2nd list 
# as its own element. So extending a list with another list combines their values.

# b = [1,2,3]
# b.extend([5,6])
# b #=> [1, 2, 3, 5, 6]

########################################################################################

# 7. Do python lists store values or pointers?
# Python lists don’t store values themselves. They store pointers to values 
# stored elsewhere in memory. This allows lists to be mutable.

# print( id(1) ) #=> 4438537632
# print( id(2) ) #=> 4438537664
# a = [1,2,3]
# print( id(a) ) #=> 4579953480
# print( id(a[0]) ) #=> 4438537632
# print( id(a[1]) ) #=> 4438537664
############################################################################################

# 8. What does “del” do?
# del removes an item from a list given its index.

# a = ['w', 'x', 'y', 'z']
# a #=> ['w', 'x', 'y', 'z']
# del a[1]
# a #=> ['w', 'y', 'z']

#############################################################################################
#9. What is the difference between “remove” and “pop”?
# .remove() removes the first instance of a matching object. Below we remove the first b.

# a = ['a', 'a', 'b', 'b', 'c', 'c']
# a.remove('b')
# a #=> ['a', 'a', 'b', 'c', 'c']
# .pop() removes an object by its index.


# a = ['a', 'a', 'b', 'b', 'c', 'c']
# a.pop(4) #=> 'c'
# a #=> ['a', 'a', 'b', 'b', 'c']
# By default, pop removes the last element from a list if an index isn’t specified.

# note => The difference between pop and del is that pop returns 
# the popped element. This allows using a list like a stack. 

############################################################################################

# 10. Remove duplicates from a list
# If you’re not concerned about maintaining the order of a list, then converting to a set and back to a list will achieve this.

# li = [3, 2, 2, 1, 1, 1]
# list(set(li)) #=> [1, 2, 3]

########################################################################################

# 11. Find the index of the 1st matching element
# For example, you want to find the first “apple” in a list of fruit. Use the .index() method.

# fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
# fruit.index('apple') #=> 2
# fruit.index('pear') #=> 0

################################################################################################

# 12. Remove all elements from a list
# Rather than creating a new empty list, we can clear the elements from an existing list with .clear().

# fruit = ['pear', 'orange', 'apple']
# print( fruit )     #=> ['pear', 'orange', 'apple']
# print( id(fruit) ) #=> 4581174216
# fruit.clear()
# print( fruit )     #=> []
# print( id(fruit) ) #=> 4581174216
# Or with del.

###############################################################################################
# 14. How to concatenate two lists
# The + operator will concatenate 2 lists.

# one = ['a', 'b', 'c']
# two = [1, 2, 3]
# one + two #=> ['a', 'b', 'c', 1, 2, 3]

#############################################################################################

# 16. Count the occurrence of a specific object in a list
# The count() method returns the number of occurrences of a specific object. Below we return the number of times the string, “fish” exists in a list called pets.

# pets = ['dog','cat','fish','fish','cat']
# pets.count('fish')
# #=> 2
####################################################################################

# 17. How to shallow copy a list?
# .copy() can be used to shallow copy a list.

# Below we create a shallow copy of round1, assign it to a new name, round2, and 
# then remove the string sonny chiba.

# round1 = ['chuck norris', 'bruce lee', 'sonny chiba']
# round2 = round1.copy()
# round2.remove('sonny chiba')
# print(round1) #=> ['chuck norris', 'bruce lee', 'sonny chiba']
# print(round2) #=> ['chuck norris', 'bruce lee']

# 18. Why create a shallow copy of a list?
# Building off the previous example, modifying round2 will modify round1 if we 
# don’t create a shallow copy.

# round1 = ['chuck norris', 'bruce lee', 'sonny chiba']
# round2 = round1
# round2.remove('sonny chiba')
# print(round1) #=> ['chuck norris', 'bruce lee']
# print(round2) #=> ['chuck norris', 'bruce lee']
# Without a shallow copy, round1 and round2 are just names pointing to the same list in memory.
#  That’s why it appears that changing the value of one changes the value of the other.

####################################################################################################
# 19. How to deep copy a list?
# For this we need to import the copy module, then call copy.deepcopy().

# difference
# Creating a shallow copy does create a new object in memory, but it’s filled with the same
#  references to existing objects that the previous list has.

# Creating a deep copy creates copies of the original objects and points to these
#  new versions. So the new list is completely unaffected by changes to the old list and vice versa.
#################################################################################################
 
# 27. Insert a value at a specific index in an existing list
# The insert() method takes an object to insert and the index to insert it at.

# li = ['a','b','c','d','e']
# li.insert(2, 'HERE')
# li #=> ['a', 'b', 'HERE', 'c', 'd', 'e']
# Note that the element previously at the specified index is shifted to the 
# right, not overwritten.

################################################################################################
# 29. Remove negative values from a list with the filter function
# Given a function, filter() will remove any elements from a sequence on which
#  the function doesn’t return True.

# Below we remove elements less than zero.

# def remove_negatives(x):
#     return True if x >= 0 else False
    
# a = [-10, 27, 1000, -1, 0, -30]
# [x for x in filter(remove_negatives, a)] 
# #=> [27, 1000, 0]
################################################################################################

# 30. Convert a list into a dictionary where list elements are keys
# For this we can use a dictionary comprehension.

# li = ['The', 'quick', 'brown', 'fox', 'was', 'quick']
# d = {k:1 for k in li}
# d #=> {'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'was': 1}

###############################################################################################
# 31. Modify an existing list with a lambda function
# Let’s take the previous map function we wrote and turn 
# it into a one-liner with a lambda.

# a = [10,20,30,40,50]
# list(map(lambda val:val*5, a))
# #=> [50, 100, 150, 200, 250]
# I could have left it as a map object until I needed to iterate over it but 
# I converted to a list to show the elements inside.

####################################################################################################
# 32. Remove elements in a list after a specific index
# Using the slice syntax, we can return a new list with only the elements up to a 
# specific index.

# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# li[:10]
# #=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 33. Remove elements in a list before a specific index
# The slice syntax can also return a new list with the values after a specified index.

# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# li[15:]
# #=> [16, 17, 18, 19, 10]
# 34. Remove elements in a list between 2 indices
# Or between two indices.

# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# li[12:17]
# #=> [13, 14, 15, 16, 17]
# 35. Return every 2nd element in a list between 2 indices
# Or before/after/between indices at a specific interval.

# Here we return every 2nd value between the indices 10 and 16 using the slice syntax.

# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
# li[10:16:2]
# #=> [11, 13, 15]

# #######################################################################################

# 50. What is the difference between sort and sorted?
# sort() modifies the list in place. sorted() returns a new list in reverse order.

# li = [10,1,9,2,8,3,7,4,6,5]
# li.sort()
# li #=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# li = [10,1,9,2,8,3,7,4,6,5]
# sorted(li) #=> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

############################################################### #########################

# 55. Find the intersection of 2 lists
# We can do this by utilizing set() with an ampersand.

# li1 = [1,2,3]
# li2 = [2,3,4]
# set(li1) & set(li2)
# #=> {2, 3}

###############################################################################################



