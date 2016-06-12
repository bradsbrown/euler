def find_bigpal():
    big_pal = 0
    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            prod = x*y
            test = str(prod)

            if test == test[::-1]:
                if prod > big_pal:
                    big_pal = prod

    return big_pal

print find_bigpal()
