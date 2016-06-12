def sum_squares(num):
    sum = 0
    for i in range(1, num+1):
        sum += i ** 2
    return sum


def square_sums(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum ** 2


def sum_square_dif(num):
    return square_sums(num) - sum_squares(num)


print sum_square_dif(100)
