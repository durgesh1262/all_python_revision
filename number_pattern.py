# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end= "")
#     print(" ")

# 1 
# 12 
# 123 
# 1234 
# 12345
##################################################################################################      
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1 , end = ' ')
#     print(" ")
            
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5           
###################################################################################################
# n = 5
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(j+1, end = " ")
#     print("")  
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

################################### make space trangle pattern ######################################################################
# n =5     #int(input("Enter number of rows"))
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ", end = " ")
#     for j in range(1,i+1):
#             print(i , end = ' ')
#     print(" ")
#       1  
#     1 2  
#   1 2 3  
# 1 2 3 4    
######################################## same as ##########################################################
# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end = " ") 
#     for j in range(i, -1, -1):
#         print(j+1 , end= " ")  
#     print("")          
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1 
########################################### asme as #############################################@@@#######
# n = 5 
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for j in range(i,-1, -1):
#         print(i+1, end= ' ')
#     print()        
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 

#############################################################################################
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(i ,end = " ")  
#     print("")    
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 
###################################################################################################

########################################## floyeds traingle ########################################################
# n=5
# number = 1
# for row in range(1,n):
#     for col in range(1, row+1):
#         print(number, end=' ')
#         number = number + 1
#     print()   
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10  
# ############################ same as previous #################################################

# n=4
# num = 1
# for row in range(1,n):
#     #for col in range(n-row-1): # for giving the space form right
#     #    print(' ', end=' ')
#     for col in range(1,row+1):
#         print(num, end=' ')
#         num = num + 2
#     print()        

# 1 
# 3 5 
# 7 9 11 
#######################################################################################################
# for i in range(5,0,-1):
#     for j in range(i+1):
#         print(j ,end = " ") 
#     print("")

# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1 

# for i in range(0,6):
#     for j in range(0,i):
#         print((i*2-1) , end=" ")
#     print()    
    
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9  

# for i in range(0,6):
#     for j in range(i,0,-1):
#         print(j ,end = " ")
#     print()    
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1
##############################################################################################
# row = 5
# for i in range(0,row + 1):
#     for j in range(row-i, 0 ,-1):
#         print(j , end = " ")
#     print()    
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
###############################################################################################
#revers pattern from 1 to 10
# start = 1
# stop = 2
# current_num = stop
# for row in range(2, 6):
#     for col in range(start, stop):
#         current_num -= 1
#         print(current_num, end=' ')
#     print("")
#     start = stop
#     stop += row
#     current_num = stop
# 1 
# 3 2 
# 6 5 4 
# 10 9 8 7 
################################################################################################
    
