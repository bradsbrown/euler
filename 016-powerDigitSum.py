def powerDigitSum(exp):
    big = 2**exp
    sum = 0
    for digit in str(big):
        sum += int(digit)
    return sum

print powerDigitSum(1000)
