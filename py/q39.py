#!/usr/bin/python

# Problem 39

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p <= 1000, is the number of solutions maximised?

# runs in 2m33.479s

from math import sqrt
from itertools import count

def sqrts( _n, _m ):
    "returns a tuple of all integral square roots between _n and _m"
    sqrt_list = []
    for i in count( _n+1 ):
        if i**2 < _m**2:
            sqrt_list.append( i )
        else:
            break
    return sqrt_list

if __name__ == "__main__":

    sqrts_of_p = [1]
    max = [0,0]

    for p in xrange( 1000 + 1 ):
        #print("p = %d" % p)
        sqrts_of_p.extend( sqrts( sqrts_of_p[-1], p ) )
        nsol = 0
        #print("  %s" % sqrts_of_p )

        for c in sqrts_of_p:
            remaining_p = p - c # the remaining perimeter
            for b in range( 1, remaining_p + 1 ):
                a = remaining_p - b
                if a > 0 and c == sqrt( a**2 + b**2 ):
                    #print("  [ %d, %d, %d ]" % ( c, b, a ) )
                    nsol+= 1
                    break

        if nsol > max[1]:
            max[0] = p
            max[1] = nsol

    print(max)

