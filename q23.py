#!/usr/bin/python

# Problem 23

# A perfect number is a number for which the sum of its proper divisors is exactly 
# equal to the number. For example, the sum of the proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
# that can be written as the sum of two abundant numbers is 24. By mathematical 
# analysis, it can be shown that all integers greater than 28123 can be written as 
# the sum of two abundant numbers. However, this upper limit cannot be reduced any 
# further by analysis even though it is known that the greatest number that cannot 
# be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of 
# two abundant numbers.

from operator import add, mul
from primes1m import primes
from itertools import combinations as c
from itertools import permutations as p
from gmpy import is_prime

MAX = 28123

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
    d.pop(n) # we only want proper divisors, so n itself should not be in the list
    return d.keys()

def sumd( n ):
    "returns a sum of all the proper divisors of n"
    return sum( divs( n ) )

def ab( n ):
    "returns true if n is abundant, else false"
    return sumd(n) > n

abundants = []
abundants_sums = {}

print( "calculating abundant numbers")

# find all the abundant numbers in this range
for i in xrange(12,MAX+1):
    if ab(i): abundants.append(i)

print( "calculating abundant numbers' sums" )

# calculate the sums of all abundant numbers in this range
for a in abundants:
    for b in abundants:
        s = a + b
        if s > MAX: break
        abundants_sums[ s ] = 1

abundants_sums = abundants_sums.keys()
cannot = [] # positive ints which can't be written as the sum of two abundants

print( "finding integers not in list of abundant numbers' sums" )

for i in xrange(1,MAX+1):
    if i not in abundants_sums:
        cannot.append( int(i) )

print( "sum of integers that are not the sum of two abundant numbers: %d" % sum(cannot) )
