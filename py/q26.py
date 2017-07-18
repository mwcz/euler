#!/usr/bin/python

# Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation 
# of the unit fractions with denominators 2 to 10 are given:
# 
#     1/2  =   0.5
#     1/3  =   0.(3)
#     1/4  =   0.25
#     1/5  =   0.2
#     1/6  =   0.1(6)
#     1/7  =   0.(142857)
#     1/8  =   0.125
#     1/9  =   0.(1)
#     1/10 =   0.1
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can 
# be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d  1000 for which 1/d contains the longest recurring 
# cycle in its decimal fraction part.

from itertools import cycle
from decimal import *
from operator import add, mul
from primes1m import primes
from gmpy import is_prime, next_prime


def pf( _num, _pf=[], _p=2 ):
    "returns the prime factorization of _num"

    assert _num >= 2

    if is_prime(_num): 
        _pf.append(_num)
        return _pf

    if _num % _p == 0:
        _pf.append(_p)
        return pf( _num / _p, _pf )
    else:
        return pf( _num, _pf, next_prime( _p ) )

def get_cycle( _n ):

    "finds the longest recurring sequence within a string (or anything that can be converted into a string)"

    n = str( _n )
    sequence = ""

    for i in xrange(len(n)): # from beginning of string to end
        for j in xrange(i): # from begining of string to i
            c = cycle( n[j:i] )
            s = ""
            while len(s) < len( n[j:] ):
                s += c.next()
            if s == n[j:] or int(s)+1 == int(n[j:]):
                sequence = n[j:i]
                break
        if len(sequence): break # break outer loop if a cycle was found

    return sequence

if __name__ == "__main__":

    #
    # finds the greatest length cycle in 1/(2..999),
    # but success is based on precision.  higher precision = longer
    # running time.
    #

    precision = 1000

    # set the precision of division
    getcontext().prec = precision

    max = (0,0,"")

    i = 2
    while i < 1000:
        s = str( Decimal(1) / Decimal(int(i)) )[2:]
        seq = get_cycle(s)
        if len(seq) > len(max[2]):
            max = (i,s,seq)
        i = next_prime(i)

    for el in max: print(el)

#    max = 0
#
#    for i in xrange(2,1000):
#        if is_prime(i):
#            max = max if max > i-1 else i-1
