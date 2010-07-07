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
from gmpy import is_prime




def pf( _num, _pf=[] ):
    "returns the prime factorization of _num"

    if _num in primes: 
        _pf.append(_num)
        return _pf

    for p in primes:
        # stop at _num/2.  would be even better to stop at sqrt(_num) once one pf over sqrt(_num) has been found
        if p > _num/2: break 
        if _num % p == 0:
            _pf.append(p)
            return pf( _num / p, _pf )




def divs( n ):
    "given a whole number n, divs() will return a list of all positive divisors of n which are less than n."
    d = {1:0}
    pfs = pf(n,[])
    for l in range(1,len(pfs)+1):
        for k in c(pfs,l): # divisors can be found by multiplying ALL combinations of the prime factors
            d[reduce( mul, k )]=0
    d.pop(n) # the number n itself should not be in the list
    return d.keys()



def d( n ):
    return sum( divs( n ) )




# build a dict for every number 2...9999, with a count for each, starting at zero
amicables = {}

# loop through all numbers 2...9999, adding 1 to the count for each number
for i in range(2,10000):
    if is_prime( i ): continue # prime numbers cannot have amicable pairs
    divsum = d(i)
    if d(divsum) == i and i != divsum:
        print( i, divsum )
        amicables[i]=0
        amicables[divsum]=0

print( sum( amicables.keys() ) )
