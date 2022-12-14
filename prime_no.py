# num = int(input('enter a number: '))
# for i in range(2,num):
#     if num % i == 0:
#         print("not primeNo")
#         break
# else:
#     print("primeNo")    
# it's a write way but not efficinet
# 
# num = int(input('enter a number: '))
# if num < 2:
#     print('number is not not primeNo')
# else:
#     for i in range(2,num):
#         if (num % i == 0):
#             print('number is not primeNo')
#             break
#     else:
#         print('primeNo')            
# # factors of the given number
# for i in range(1,num+1):
#     if(num % i == 0):
#         print(i , end=" ")
    

# prime no in the given range
# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if number % i == 0:  
#                 break  
#         else:  
#             print (number, end=' ')          

# for practice

  

######### finding the prime factors #################################
# n = int(input("Enter the number for calculating the prime factors :\n"))
# mylist = []
# i = 2
# while n != 1:
#     rem = n % i
#     if ( rem == 0 ):
#         n = n / i
#         mylist.append(i)
#         print(i)
#     else:
#         i = i + 1
# print(mylist)        
# print('sum of all factors: ',sum(mylist))


########################################## for practic prime no in given range: ####################

# n = int(input("Please enter a number: "))
# for i in range(1,n+1):
#     if i > 1:
#         for j in range(1,n):
#             if i % 2 == 0:
#                 break
#         else:
#             print(i, end = ' ')   
# 
#  
# i = 1
# n = 6
# while i < 5:
#     n -= 1
#     for i in range(1,n):
#         for j in range(i,6):
#             print(j, end = " " )
#             i = i+1
#         print()    

###############################################################################
######################## using lambda function #################################################################
 
# lambda function panding #################################################################
# prime = lambda num : print('not prime') if num % 2 == 0 else print('prime')
# n = prime(21)

