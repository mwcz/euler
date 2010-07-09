#!/usr/bin/python

# Problem 48

# The series, 
# 
#     1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# 
# Find the last ten digits of the series, 
# 
#     1^1 + 2^2 + 3^3 + ... + 1000^1000.

ans = sum( [ n**n for n in range(1,1001) ] ) % 10**10

print( ans )

