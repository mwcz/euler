#!/usr/bin/python

# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 
#     1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# 
#     (1 + 2 + ... + 10)^2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 
# 
#     3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

nats = range( 1, 101 )

s1 = reduce( lambda a, b: a + b, map( lambda x: x**2, nats ) )
s2 = reduce( lambda a, b: a + b, nats ) ** 2

print( abs( s1 - s2 ) )
