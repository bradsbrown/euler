def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def biggestPrimeFactor(num):
    list = [1]
    for x in range(2, (int(num**0.5))):
        if x % 2 != 0:
            if num % x == 0 and isPrime(x):
                print x
                list.append(x)
    return list[-1]


print biggestPrimeFactor(600851475143)
