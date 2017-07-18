#!/usr/bin/python

# Problem 20

# n! means n * (n * 1) * ... * 3 * 2 * 1
# 
# Find the sum of the digits in the number 100!

from math import factorial as f

print( sum( [ int(n) for n in str( f(100) ) ] ) )
