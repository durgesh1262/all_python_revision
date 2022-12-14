# def fibo(num):
#     if num == 1:
#         print(num)
#     else:
#         a = 0
#         b = 1
#         print(a)
#         print(b)
#         i = 1
#         while i < num:
#        # # for i in range(2, num):
#             c = a + b
#             a , b = b , c
#             i = i + 1
#             print(c)
# num = fibo(int(input('enter a number: ')))          

######################################################## recursive fuctions ka use kana jyda rahi hai###########
# fibonacci series of using recursive function
# def fibonacci(i):
#     if (i == 0):
#         return 0
#     elif (i == 1):
#         return 1    
#     else:
#         return fibonacci(i-2) + fibonacci(i-1)    
# for x in range(13):
#     print(fibonacci(x), end=" ")


# ##### for prectice ###################################
# def fibo(num):
#     if (num == 0):
#         return 0
#     elif (num == 1):
#         return 1
#     else:
#         return fibo(num-2) + fibo(num-1)    

# for x in range(10):
#     print(fibo(x), end=" ")