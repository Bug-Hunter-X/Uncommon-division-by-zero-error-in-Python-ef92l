def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of a=0
    if b == 0:
        return a  # Correct handling of b=0
    return a / b

result = function_with_uncommon_error(10, 0)
print(result) # This will correctly print 10 

result = function_with_uncommon_error(0, 0) # Uncommon error scenario
print(result) # This will correctly print 0