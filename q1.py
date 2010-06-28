#!/usr/bin/python

# Problem 1

# If we list all the natural numbers below 10 
# that are multiples of 3 or 5, we get 3, 5, 
# 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 
# 5 below 1000.

NUM = 1000

numbers = {}
sum = 0
x = 0

while True:
    x += 3
    if x >= NUM: break
    numbers[x] = 1

x = 0

while True:
    x += 5
    if x >= NUM: break
    numbers[x] = 1

for val in numbers.keys():
    sum += val

print( numbers.keys() )
print( "The sum of all multiples of 3 or 5 below %d is: %d" % ( NUM, sum ) )
