#!/usr/bin/python

# Problem 40

# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
# 
# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000

n = ''
for i in xrange(1,1000000+1):
    n += str(i)

print( int(n[     0]) * 
       int(n[     9]) * 
       int(n[    99]) * 
       int(n[   999]) * 
       int(n[  9999]) * 
       int(n[ 99999]) * 
       int(n[999999]) )
