def find_prod():
    for x in range(1, 1000):
        for y in range(1, 1000):
            z_sq = x**2 + y**2
            z = z_sq**0.5
            if x + y + z == 1000:
                return x * y * z

print find_prod()
