# def factorial(num):
#     if (num == 0 or num == 1):
#         return 1
#     else:
#         return num * factorial(num-1)
# num = factorial(0)
# print(num)

facto = lambda x: 1 if x == 0 else x*facto(x-1)
num= facto(5)
print(num)

