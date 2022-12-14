#Q.40 Write a program to find out reverse of a given number.
num = int(input('enter the number: '))
reverse_no = 0
while num > 0:
    digit = num % 10
    reverse_no = reverse_no * 10 + digit
    num = num // 10
print(reverse_no)  