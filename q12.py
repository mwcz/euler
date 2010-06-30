#!/usr/bin/python

# Problem 12

# The sequence of triangle numbers is generated by adding the natural 
# numbers. So the 7th triangle number would be 
# 
#     1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# 
# The first ten terms would be:
# 
#     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
# 
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?

from operator import add
from math import factorial as f
from primes1m import primes

def pf( _num, _pf=[] ):
    "returns the prime factorization of _num"

    if _num in primes: 
        _pf.append(_num)
        return _pf

    for p in primes: # would be much faster if this didn't loop over ALL primes, only primes 2.._num/2
        if _num % p == 0:
            _pf.append(p)
            return pf( _num / p, _pf )

def divs( _pf=[] ):
    "given a list of prime factors, returns the number of positive divisors"
    up = {}
    for p in _pf:
        up[p]=1
    up = up.keys() # up now holds the unique primes
    d = 1
    for p in up:
        d *= 1 + _pf.count(p)
    return d

# unused.  this approach was interesting but not optimal (maybe would't work at all)
def c( n, r ):
    "returns the number of r-combinations of n elements"
    return f(n) / ( f(r) * f(n-r) )

i = 2
t = 3
max = 2

while True:

    p = pf( t, [] )
    num_divs = divs( p )
    max = max if max >= num_divs else num_divs

    print( i, t, max, p, num_divs )

    if num_divs > 500:
        break
    
    i += 1
    t += i
