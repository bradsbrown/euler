from Euler import isPrime


def countQuadPrimes(a, b):
    n = 0
    count = 0
    while True:
        quadRun = n*n + a*n + b
        if isPrime(quadRun):
            count +=1
            n += 1
        else:
            break
    return count


def quadPrimes(absLim):
    maxCount, maxA, maxB = 0, 0, 0
    for a in range(-absLim, absLim):
        for b in range(-absLim, absLim):
            count = countQuadPrimes(a, b)
            if count > maxCount:
                maxCount, maxA, maxB = count, a, b

    return maxA * maxB


print quadPrimes(1000)
