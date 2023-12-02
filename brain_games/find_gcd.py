def find_gcd(num1, num2):
    if num1 == num2:
        return num1
    if num1 == 0 or num2 == 0:
        return "divided by zero"
    if not num1 % num2:
        return num2
    if not num2 % num1:
        return num1
    if num1 > num2:
        greater_num = num1
        less_num = num2
    else:
        greater_num = num2
        less_num = num1
    temp_nod = 1
    for iter in range(2, int((less_num / 2) + 1)):  
        if not num1 % iter and not num2 % iter:
            temp_nod = iter            
    return temp_nod    
