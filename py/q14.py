#!/usr/bin/python

# Problem 14

# The following iterative sequence is defined for the set of positive integers:
# 
#     n -> n/2 (n is even)
#     n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
#     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

counts = {}

def s( n, c=1 ):
    "n is the number, c is the chain length (count)"
    if n == 1: return c
    if counts.has_key(n): return counts[n] + c
    return s( n/2 if n%2==0 else 3*n+1, c+1 )

max = [-1,-1]

for i in xrange(1,1000000,2):
    m = s(i)
    counts[i] = m
    if m > max[1]:
        max[0] = i
        max[1] = m

print( max )
