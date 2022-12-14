#Q.17 Write a program accepts a number from user and check 
#given number is even or odd. 

# num = int(input('enter a no.: '))
# if num%2 == 0:
#     print('its even number: ', num)
# else:
#     print('its odd number')

###############################################################################################
#Q.18 Write a program accepts three numbers from user and 
#calculate biggest number out of two numbers.

# first_no = int(input('enter the first_no: '))
# second_no = int(input('enter the second_no: '))
# third_no = int(input('enter the third_no: '))
# if (first_no>second_no) and (first_no>third_no):
#     print('biggest number is: ',first_no)
# elif (second_no>third_no) and (second_no>first_no):
#     print('second_no is bigest',second_no)    
# else:
#     print('third is bigest', third_no)

###############################################################################################
#Q.20 Write a program accepts a number from user and check 
#given number is palindrome number or not. 

# n = input('enter a number: ')

# re = n[::-1]
# if n == re:
#     print('number is palindrome')
# else:
#     print('number is not palindrome')    
############################# real way #######################################
# n = int(input('enter a number:'))
# rev = 0
# temp = n
# while n > 0:
#     digit =  n % 10
#     rev = rev * 10 + digit
#     n = n//10
# print(rev)    
# if temp == rev:
#     print('number is palindrome')
# else:
#     print('number is not palindrome')     

#############################################################
# Q.21 Write a program accepts a number from user and check 
#given number is Armstrong number or not.

# num = 153
# temp = num
# length = len(str(num))
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum = digit**length + sum
#     temp = temp // 10
# if sum == num:
#     print('armstromg number')
# else:
#     print('armstromg number nahi hai')     

###############################################################################################
#Q.22 Write a program accept a three digits number from user 
#and check biggest digit of given number

# num = 159
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10

# if a>b and a>c:
#     print('{} is grater'.format(a))
# elif b>a and b>c:
#     print('{} is grater'.format(b))
# else:
#     print('{} is grater'.format(c))            

###############################################################################################
# Q.25 Write a program to calculate whether character is in 
#lowercase or uppercase. 

# ch = input('enter a character: ')
# if (ch>= 'A') and (ch<= 'Z'):
#     print('{} is in uppercase'.format(ch))
# elif ch>='a' and ch<='z':
#     print('{} is in lowercase'.format(ch))
# else:
#     print('{} in not in lower case or not in uppercase')        

#######  other way ##########
# ch = input("Please Enter Your Own Character : ")

# if(ch.isupper()):
#     print("The Given Character ", ch, "is an Uppercase Alphabet")
# elif(ch.islower()):
#     print("The Given Character ", ch, "is a Lowercase Alphabet")
# else:
#     print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
#################################################################################

#Q.27 Write a program to calculate whether a character is vowel or consonant.

# ch= input('Enter a character:')
# if (ch =='a'or ch =='e' or ch == 'i' or ch =='o'or ch =='u'or ch =='A'or ch == 'E'or ch =='I' or ch == 'O'or ch =='U'):
#     print("The Given Character in vowel")
# else:
#     print("The Given Character is consonant")   
##############################################################################################
#Q.28 Write a program that accepts five subjects� marks from user and calculate the total marks then calculate 
#Percentage. Display message according to following 
#condition. 
#Percentage >=60 then print message Grade APercentage >=50 then print message Grade BPercentage >= 40 then print message Grade C 
#Percentage < 40 then print message Grade D
# my_dictionary = {}
# for i in range(5):
#     subject_name = input("Enter a subject name: ")
#     subject_marks = input("Enter a subject marks: ")
#     my_dictionary[subject_name] = subject_marks
# print(my_dictionary)
# mylist = []
# for j in my_dictionary:
#     mylist.append(int(my_dictionary[j]))
# add = sum(mylist)
# persentage = add*100/500
# print(persentage)
###############################################################################################
# Q.29 Write a program for generating electricity Bill. Acceptlast month unit and current month unit from user, then 
# calculate and print bill amount according to following 
# condition 
# 0-150 charges 4 rs/unit 
# 151-300 charges 6 rs/unit 
# 301-500 charges 8rs/unit 
# >500 charges 10rs/unit
##################################################################################################    
# Q.30 Write a program to accept basic salary from user, if 
# basic salary is between 0 and 15000 then TA is 8% of basicsalary, DA is 4% of basic salary. 
# If salary is above 15000 then TA is 10% of basic salary, DA is5% of basic. 
# Calculate gross salary as gs=basic salary+TA+DA?



