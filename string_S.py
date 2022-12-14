# str is immutable. 
# .Slicing Strings

# mystr = 'xyzdurgeshbsdfjiodf'
# print(mystr[10:3:-1])
#####################################################################################################
# .Modify A String

# # Return the string in lower case
# txt = 'Learning is a constant process of discovery'
# print(txt.lower()) ## or txt.upper()
# Output:
# learning is a constant process of discovery

###########################################################################################
# String Concatenation
# Code:

# #Create two separate strings and add them together using +
# n = 'Learning a new thing '
# a = 'EVERYDAY!'
# t = n + a
# print(t)
##############################################################################################
# Count The Number Of Vowels In A String
# Code:

# #Create a function that checks if a string sontains a vowel
# def vowel (word):
#   count = 0
#   vowel = set('aeiouAEIOU')

#   for char in word:
#     if char in vowel:
#       count = count + 1

#   print('The number of vowels in this string: ', count)

# word = 'Learning a new thing everyday.'
# print(vowel(word))

###############################################################################################

# roated strings
# string =  'python is greate language'
# print(string[-3:] + string[:-3])

# output = agepython is greate langu

###############################################################################################
# shorting the given string
# string = 'python is greate'
# shorted_str = str(sorted(string))
# print(string.split(' '))
#############################################################################################

#Create A Database
# JO BHI FILE ME DATA HAI VO TERMINAL ME PRINT HO JAYEGA.
file = open('companyA.txt')
print(file.read())
file.close()

