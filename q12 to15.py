# Q.12 Write a program accepts three numbers from user and 
# calculate average of given three numbers. 
# form my logic to calculate average
# sum = 0
# for i in range(3):
#     num = int(input('enter numbers: '))
#     sum = sum + num
# avg = sum /3
# print(avg)
# # form googlw way to calculate average
# a = int (input(" Please Enter the First Number: ")) 
# b = int (input(" Please Enter the second number: "))
# c = int (input(" Please Enter the third number: "))
# average=(a+b+c)/3
# print("The average of three numbers is ", average)

# Q.13 Write a program accepts 4 digits no. and display the no. 
# in reverse order
# num = 1234
# rev_num = 0
# while num > 0:
#     digit = num % 10
#     rev_num = rev_num * 10 + digit
#     num = num//10
# print(rev_num) 


# other logic
# num = 123456
# print(str(num)[::-1])

# Q.14 Write a program accepts an amount in rupees (Hint Rs4567) and 
# find out how many currency of Rs2000,500,200,100,50,20,10,5,2,1. 
#Control Flow (if-Elif) 

# def no_notes(a):
#   Q = [2000,500, 200, 100, 50, 20, 10]
#   x = 0
#   for i in range(7):
#     q = Q[i]
#     x += int(a / q)
#     a = int(a % q)
#   if a > 0:
#     x = -1
#   return x
# print(no_notes(880))
# print(no_notes(1000))

# def note_counter(rupees):
#     for i in range(7):
#         notes = [2000,500,200,100,50,20,10]
#         no_of_notes = 0
#         single_note = notes[i]
#         no_of_notes = int(rupees/single_note) + no_of_notes
#         rupees = int(rupees%single_note)
    
#     if rupees > 0:
#         no_of_notes-=1
#         return no_of_notes    

# print(note_counter(1000))
################################## other way and best way ###################################
# amount = int(input('enter the amount: '))
# while amount > 0:
#     if amount >= 2000:
#         print('no. of 2000 note: ', int(amount/2000))
#         amount = amount % 2000
#     elif amount >= 500:
#         print('no. of 500 note: ', int(amount/500))
#         amount = amount % 500
#     elif amount >= 200:
#         print('no. of 200 note: ', int(amount/200))
#         amount = amount % 200
#     elif amount >= 100:
#         print('no. of 100 note: ', int(amount/100))
#         amount = amount % 100
#     elif amount >= 50:
#         print('no. of 50 note: ', int(amount/50))
#         amount = amount % 50
#     elif amount >= 20:
#         print('no. of 20 note: ', int(amount/20))
#         amount = amount % 20
#     elif amount >= 10:
#         print('no. of 10 note: ', int(amount/10))
#         amount = amount % 10
#     elif amount >= 5:
#         print('no. of 5 note: ', int(amount/5))
#         amount = amount % 5
#     elif amount >= 2:
#         print('no. of 1 note: ', int(amount/2))
#         amount = amount % 2
#     elif amount >= 1:
#         print('no. of 1 note: ', int(amount/1))
#         amount = amount % 1                                                                

#########################################################################################
#Q.16 Write a program accepts two numbers from user and 
#calculates first no is divisible by second or not. 
# i = 1
# while i<5:
#     first_no = int(input('enter the first_no: '))
#     second_no = int(input('enter The second no: '))
#     if first_no%second_no == 0:
#         print('1st is devisiblie by second_no')
#     else:
#         print('not devisiblie')
#     i +=1

