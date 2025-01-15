def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0 #Explicitly handle the a=0 and b=0 case
    if a == 0:
        return b
    if b == 0:
        return a
    return a / b

result = function_with_uncommon_error_solution(10, 0)
print(result) # This will correctly print 10

result = function_with_uncommon_error_solution(0, 0) #Corrected handling for both 0
print(result)  # This will correctly print 0