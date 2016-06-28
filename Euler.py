def listPrimes(n):
    '''returns a list of primes up to a max size n'''
    sieve = [True] * (n/2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n/2) if sieve[i]]


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5

    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True
