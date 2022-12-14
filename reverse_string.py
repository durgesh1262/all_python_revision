# mystr = 'i am the best man in the world.'
# mynum = '123'
# print(mystr[::-1])
# print(mynum[::-1])

#Using for loop
real_str = "mystr"
string = ""
for i in real_str:
    string = i + string
print(string)

# Using while loop( solve ni ho raha hai)
# real_str = "mystr"
# count = len(real_str)
# rev_string = ""
# while count > 0:
#     rev_string += real_str[count-1]
#     count -= 1
# print(real_str)    
# 
# Using recursion 

# def reverse(s):
#     if len(s) > 0:
#         print(s[len(s)-1], end = "")
#         reverse(s[:len(s)-1])
# reverse('sita ram')