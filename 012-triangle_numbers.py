def countFactors(num):
    lim = int((num**0.5) + 1)
    factors_count = 0
    for i in range(1, lim):
        if num % i == 0:
            factors_count += 2
    return factors_count


def triangle_by_divisors(divs):
    # first, start a list of triangle numbers
    tri = 1
    i = 2
    cont = True
    while cont:
        if countFactors(tri) > divs:
            cont = False
            return tri
        else:
            tri += i
            i += 1

print triangle_by_divisors(500)
