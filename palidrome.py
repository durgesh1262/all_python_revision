################ using slising oparator ###############
# value = input("enter some value: ")
# palin = value[::-1]
# if (palin == value):
#     print("its palindrome value")
# else:
#     print("its not palindrome value")

################### using for loop #####################

value = input("enter some value: ")
rev_value = ""
for i in value:
    rev_value = i + rev_value
if rev_value == value:
    print("its palindrome value")
else:
    print("its not palindrome value")

