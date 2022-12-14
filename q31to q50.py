# Q.31Write a program that accepts a character and check given 
# character is vowel or not by using switch case.

# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "JavaScript":
#         print("You can become a web developer.")

#     case "Python":
#         print("You can become a Data Scientist")

#     case "PHP":
#         print("You can become a backend developer")
    
#     case "Solidity":
#         print("You can become a Blockchain developer")

#     case "Java":
#         print("You can become a mobile app developer")
#     case _:
#         print("The language doesn't matter, what matters is solving problems.")

#################################################################################################
# Q.32 Write a program to show day of week according to user 
# input by using switch case. 

# Q.33 Write a program to show name of month according to 
# user input by using switch case. 

# Q.34 Write a program to perform all arithmetic operationsaccording to user choice (for ex-for addition press �+�...) by 
# using switch case.
##############################################################################################
#Q.37 Write a program to calculate factorial of a given number
# num = int(input('enter the number: '))
# def factorial(num):
#     for i in range(num):
#         if num == 0 or num  == 1:
#             return 1
#         else:
#             return num * factorial(num - 1)

# fact = factorial(num)    
# print(fact)     

# facto = lambda n: 1 if n == 0 else n*facto(n -1)
# print(facto(12))
###############################################################################################
#Q.40 Write a program to find out reverse of a given number.
# num = int(input('enter the number: '))
# reverse_no = 0
# while num > 0:
#     digit = num % 10
#     reverse_no = reverse_no * 10 + digit
#     num = num // 10
# print(reverse_no)     
# ##############################################################################################
# Q.41 Write a program that accepts a number from user and 
# check given number is palindrome number or not.

# num = int(input('enter the number: '))
# check_palindrome = num
# reverse_no = 0
# while num > 0:
#     digit = num % 10
#     reverse_no = reverse_no * 10 + digit
#     num = num // 10

# if check_palindrome == reverse_no:
#     print('its palindrome no')
# else:
#     print('its not palindrome')    

################################################################################################
# Q.42 Write a program that accepts a number from user and 
# check given number is Armstrong number or not. 

num = input('enter the number: ')
order = int(len(num))
temp = int(num)
sum = 0
while temp > 0:
    digit = temp % 10
    sum = digit**order + sum
    temp = temp // 10
if int(num) == sum:    
    print('its palindrome')
else:
    print('its not palindrome')    