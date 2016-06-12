from itertools import count

for i in count(20):
    if all(map(lambda x: i % x == 0, range(1, 21))):
        print i
        break

    # num = 20
    # match = False
    # while not match:
    #     test = True
    #     if num % 11 != 0:  # prime
    #         test = False
    #     if num % 12 != 0:  # cover 6, 2
    #         test = False
    #     if num % 13 != 0:  # prime
    #         test = False
    #     if num % 14 != 0:  # covers 7, 2
    #         test = False
    #     if num % 15 != 0:  # covers 5 3
    #         test = False
    #     if num % 16 != 0:  # cover 8, 2
    #         test = False
    #     if num % 17 != 0:  # prime
    #         test = False
    #     if num % 18 != 0:  # covers 3, 2
    #         test = False
    #     if num % 19 != 0:  # prime
    #         test = False
    #     if num % 20 != 0:  # covers 10, 2
    #         test = False
    #     if test:
    #         match = True
    #         return num
    #     else:
    #         num += 1


# print findSmallest()
