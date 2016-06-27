def facDigitSum(num):
    fac = 1
    sum = 0
    for i in range(1, num + 1):
        fac *= i
    for dig in str(fac):
        sum += int(dig)
    return sum

print facDigitSum(100)
