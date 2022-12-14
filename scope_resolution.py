temp = 10
def func(self):
    global temp
    temp = 20
    print(temp)
    # return temp
print(temp)
print(temp)
i=func(temp)
# print(i) 
print(temp)   