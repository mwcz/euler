#!/usr/bin/python

# Problem 19

# You are given the following information, but you may prefer to do some research for 
# yourself.
# 
#  -  1 Jan 1900 was a Monday.
# 
#  -  Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
# 
#  -  A leap year occurs on any year evenly divisible by 4, 
#     but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 
# 1901 to 31 Dec 2000)?

def ily( y ):
    "is leap year?"
    return True if y%4==0 and y%100!=0 or y%400==0 else False

m = [31]*12 # months
m[1] = 28 # feb
m[3] = 30
m[5] = 30
m[8] = 30
m[10] = 30

current_day = 1 # jan 1 1901 is a tuesday

sundays = 0

for year in xrange(1901,2001):
    m[1] = 29 if ily(year) else 28
    for month in m:
        for day in range(month):
            if day == 0 and current_day == 6: sundays += 1
            current_day += 1
            current_day %= 7

print(sundays)
