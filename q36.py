#!/usr/bin/python

# Problem 36

# The decimal number, 585 = 10010010012 (binary), is 
# palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, 
# which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either 
# base, may not include leading zeros.)

from itertools import count
from math import log

def base2( _num ):

    "converts a base-10 number _num to base-2"

    result = ""

    lg = int(log(_num,2))

    while lg >= 0:
        d = _num / 2**lg
        _num -= d * 2**lg
        result += str(d)
        lg -= 1

    return int(result)

def is_pdrome( _s ):

    s = str(_s)

    if len( s ) in (0,1): 
        return True

    if s[0] == s[ len(s) - 1 ]: 
        return is_pdrome( s[ 1 : len(s) - 1 ] )

    return False

if __name__ == "__main__":

    s = []

    for n10 in xrange(1,1000000):
        n2 = base2( n10 )
        if is_pdrome(n2) and is_pdrome(n10): 
            print( n10,n2)
            s.append(n10)

    print("sum of all numbers < 1e6 which are palindromic in base 10 and base 2: %d" % sum(s) )


