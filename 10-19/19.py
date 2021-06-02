# ... How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1900
month = 1
day = 1
weekday = 2

first_sundays = 0

def leap_year():
    global month, weekday
    if (year % 4 != 0):
        month += 1
        weekday += 28
        weekday %= 7
    elif (year % 100 == 0 and year % 400 != 0):
        month += 1
        weekday += 28
        weekday %= 7
    else:
        month += 1
        weekday += 29
        weekday %= 7

def increment_month():
    global year, month, weekday
    if (month == 2):
        leap_year()
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        month += 1
        weekday += 30
        weekday %= 7
    else:
        month += 1
        weekday += 31
        weekday %= 7
        if (month == 13):
            month %= 12
            year += 1
        

while (year < 2001):
    increment_month()
    if (weekday == 1 and year > 1900):
        first_sundays += 1

print(first_sundays)
# answer equals 171