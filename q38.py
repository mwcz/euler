#!/usr/bin/python

# Problem 38

# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
#     192 * 1 = 192
#     192 * 2 = 384
#     192 * 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 
# 192384576. We will call 192384576 the concatenated product 
# of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which 
# is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can 
# be formed as the concatenated product of an integer with 
# (1,2, ... , n) where n > 1?

def is_pandigital( _s ):

    s = str(_s)

    l = [ int(c) for c in s ]
    l.sort()

    return l == [1,2,3,4,5,6,7,8,9]

from itertools import count

if __name__ == "__main__":

    for n in count(1):

        concat = ""

        for m in count(1):

            prod = n*m
            if len(str(prod)) > 9 - len(concat): break
            concat += str(prod)

        if is_pandigital(concat):
            print(concat)


