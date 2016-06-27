import datetime
#
# months = {1: 31,
#           2: 28,
#           3: 31,
#           4: 30,
#           5: 31,
#           6: 30,
#           7: 31,
#           8: 31,
#           9: 30,
#           10: 31,
#           11: 30,
#           12: 31}
#
# def isLeapYear(year):
#     if year % 4 == 0:
#         if year % 100 != 100:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     return False


def incrementDay(day, month, year):
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

    return 1, month, year


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2.
    Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def countSundays(d1, m1, y1, d2, m2, y2):
    assert not dateIsBefore(y2, m2, d2, y1, m1, d1)
    sundays = 0
    # if start date is not a 1st of month, reset to next month start
    if d1 != 1:
        d1, m1, y1 = incrementDay(d1, m1, y1)

    # check each start of month for a Sunday
    while dateIsBefore(y1, m1, d1, y2, m2, d2):
        if datetime.datetime(y1, m1, d1).weekday() == 6:
            sundays += 1
        d1, m1, y1 = incrementDay(d1, m1, y1)

    return sundays


print countSundays(1, 1, 1901, 31, 12, 2000)
