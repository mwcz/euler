#!/usr/bin/python

# Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the 
# factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial as f
from itertools import count

def curious( n ):
    
    return n == sum( map( f, [ int(c) for c in str(n) ] ) )

if __name__ == "__main__":

    s = 0
    for i in xrange(3,100000):
        if curious(i):
            s += i
            print(s)
