#!/usr/bin/python

# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:
# 
#     F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
# 
# Hence the first 12 terms will be:
# 
#     F(1)  = 1
#     F(2)  = 1
#     F(3)  = 2
#     F(4)  = 3
#     F(5)  = 5
#     F(6)  = 8
#     F(7)  = 13
#     F(8)  = 21
#     F(9)  = 34
#     F(10) = 55
#     F(11) = 89
#     F(12) = 144
# 
# The 12th term, F(12), is the first term to contain three digits.
# 
# What is the first term in the Fibonacci sequence to contain 1000 digits?

from math import sqrt 

# f = lambda n: long((((1+sqrt(5))/2)**n-(1-((1+sqrt(5))/2))**n)/sqrt(5))
# 
# i = 1
# while True:
#     f_i = f(i)
#     print( f_i )
#     if len(str(f_i)) >= 1000:
#         break
#     i += 1

a = 1
b = 1
c = a + b
i = 2

while len(str(c)) != 1000:
    c = a + b
    a = b
    b = c
    i += 1

print(i)
