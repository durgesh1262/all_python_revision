def decor_result(result_function):
    def Distantion(marks):
        for m in marks:
            if m >= 75:
                print('DISTANTION')
        result_function(marks)
    return Distantion            

@decor_result
def result(marks):
    for m in marks:
        if m > 33:
            pass
        else: 
            print("FAILED")
            break
    print("PASSED")    
result([48,69,60,59,78,76,79])    