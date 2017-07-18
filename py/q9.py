#!/usr/bin/python

# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
#     a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

nums = range( 1, 1001 )

for a in nums:
    for b in nums:
        for c in nums:
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print( a, b, c )

# this is pretty slow, so the answer is a = 200, b = 375, c = 425
