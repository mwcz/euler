#!/usr/bin/python

# Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers 
# less than n which divide evenly into n).
# 
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable 
# pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

from operator import add, mul
from math import factorial as f
from primes1m import primes
from itertools import combinations as c



def pf( _num, _pf=[] ):
    "returns the prime factorization of _num"

    if _num in primes: 
        _pf.append(_num)
        return _pf

    for p in primes: # would be much faster if this didn't loop over ALL primes, only primes 2.._num/2
        if _num % p == 0:
            _pf.append(p)
            return pf( _num / p, _pf )

def divs( n ):
    "given a list of prime factors, returns a list of positive divisors"
    d = {1:0}
    pfs = pf(n)
    for l in range(1,len(pfs)+1):
        for k in c(pfs,l):
            d[reduce( mul, k )]=0
    return d.keys()

def d( n ):
    return divs( pf( n, [] ) )

amicables = {}

for i in range(2,1000):
    print(i)
    divisors = divs(i)
    divisor_sum = sum( divisors )
    amicables[ divisor_sum ] = 0

print(amicables)
