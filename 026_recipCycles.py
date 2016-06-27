from decimal import *

def findLongest(maxDiv):
    longest = 1
    d = 1
    getcontext().prec = 2000
    for x in range(1, maxDiv):
        whole = str(Decimal(1)/Decimal(x))[2:]
        for y in range(1, 1000):
            print y
            if whole[:y] == whole[y:y*2]:
                if y > longest:
                    longest = y
                    d = x

    return d

print findLongest(1000)
