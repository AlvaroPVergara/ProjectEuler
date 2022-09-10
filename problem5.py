mcm=1

def factornum(num:int):
    """Function for factoring numbers (used to solve problem 3)"""
    pfactors = []
    while (num != 1):
        i = 2
        while (num % i != 0 and i != num):
            i += 1
        num = num / i
        pfactors.append(i)
    pfactors.sort()
    return pfactors

def greatest_common_divisor(num1:int, num2:int):
    """Function that returns the greatest common divisor of two numbers"""
    factors1=factornum(num1)
    factors2=factornum(num2)
    maxfactors =factors1.copy()
    for elem in factors2:
        if elem not in factors1:
            for times in range(factors2.count(elem)):
                maxfactors.append(elem)
        else:
            if factors2.count(elem)>maxfactors.count(elem):
                for times in range(factors2.count(elem)-maxfactors.count(elem)):
                    maxfactors.append(elem)
    total=1
    for number in maxfactors:
        total=total*number
    return total


for num in range(1,21,1):
    if mcm%num!=0:
        mcm=greatest_common_divisor(mcm, num)
print(mcm)