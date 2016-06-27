def sumNonAbunds():
    LIM, tot = 28124, 0
    abundants = set()

    for n in range(1, LIM):
        if d(n) > n:
            abundants.add(n)
        if not any((n-a in abundants) for a in abundants):
            tot += n

    return tot


def d(n):
    s = 1
    t = n**0.5
    for i in range(2, int(t)+1):
        if n % i == 0:
            s += i + n/i
    if t == int(t):
        s -= t
    return s

print sumNonAbunds()
