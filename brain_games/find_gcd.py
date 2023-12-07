def find_gcd(num1, num2):
    if num1 == num2:
        return num1
    if not num1 % num2:
        return num2
    if not num2 % num1:
        return num1
    less_num = num2 if num1 > num2 else num1
    nod = 1
    for iter in range(2, int(less_num / 2) + 1):
        if not num1 % iter and not num2 % iter:
            nod = iter
    return nod
