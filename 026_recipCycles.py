from Euler import listPrimes


def findLongest(d):
    for p in listPrimes(d)[::-1]:
        period = 1
        while pow(10, period, p) != 1:
            period += 1
        if p-1 == period:
            break

    return p


print findLongest(1000)
