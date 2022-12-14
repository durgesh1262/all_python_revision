# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1		
	#return 2		
	yield 3	# yield return value, but not stop the generator function, it only puse the generator function 	

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)
