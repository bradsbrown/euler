def distinctPowers(max):
    base = range(2, max+1)
    power = range(2, max+1)
    distPows = []
    for a in base:
        for b in power:
            if a**b not in distPows:
                distPows.append(a**b)

    return len(distPows)


print distinctPowers(100)
