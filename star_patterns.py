
# for i in range(0,5):
#     for j in range(0,i+1):
#         print('*' ,end = " ")
#     print()    
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
#######################################################################################################
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print('*' ,end = " ")
#     print()  

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
#############################################################################################
# for i in range(5, 1, -1):             
#     for j in range(i):
#         print('@ ', end= '')
#     print()    

# @ @ @ @ @ 
# @ @ @ @ 
# @ @ @ 
# @ @ 
################################################################################################
# n =5
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end= ' ')
#     for j in range(i+1):
#         print( ' # ', end= ' ')   
#     print(' ')     
#          #   
#        #   #   
#      #   #   #   
#    #   #   #   #   
#  #   #   #   #   #      
######################################################################################################
# n =5
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ', end= ' ')
#     for j in range(i+1):
#         print( ' * ', end= ' ')   
#     print(' ')  
# N = 5
# for i in range(N-1,-1,-1):
#     for j in range(N-i-1):
#         print(' ' ,end= " ")
#     for j in range(i+1):
#         print(' * ' , end=" ")  
#     print("") 
#      *   
#        *   *   
#      *   *   *   
#    *   *   *   *   
#  *   *   *   *   *   
#  *   *   *   *   *  
#    *   *   *   *  
#      *   *   *  
#        *   *  
#          *      
    
###################################################################################################
# word = "Python"
# lenght = len(word)

# for row in range(lenght):
#     for col in range(row+1):
#         print(word[col] , end = " ")
#     print()    
# P 
# P y 
# P y t 
# P y t h 
# P y t h o 
# P y t h o n    

###################################################################################################
# ascii_number = 65
# rows = 7
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         character = chr(ascii_number)
#         print(character, end=' ')
#         ascii_number += 1
#     print(" ") 

# A  
# B C  
# D E F  
# G H I J  
# K L M N O  
# P Q R S T U  
# V W X Y Z [ \
# ##########################################################################################     