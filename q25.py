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

# the gmpy package (python bindings for the gnu multiple precision
# library) comes with a fib function that almost certainly uses
# binet's formula.  
# 
# 

from gmpy import *

i = 1

while True:
    f_i = len(str(fib(i)))
    if f_i >= 1000:
        print(i)
        break
    i += 1
    

# first approach using Binet's closed form of the Fib sequence.
# didn't work becuase 2.0**1023 is the largest fp number python
# can handle.  this solution requires at least phi**4782, so it
# crashes.
#
# c1 = (1+sqrt(5))/2
# c2 = 1 - (1+sqrt(5))/2
# c3 = 1/sqrt(5)
# 
# def f(n):
#     return long((c1**n-(c2)**n)*c3)
# 
# i = 1
# while True:
#     f_i = f(i)
#     print( i )
#     if len(str(f_i)) >= 1000:
#         break
#     i += 1

# second solution, iterative.  runs in:
#
# real    0m1.553s
# user    0m1.544s
# sys 0m0.000s
# 
# a = 1
# b = 1
# c = a + b
# i = 2
# 
# while len(str(c)) != 1000:
#     c = a + b
#     a = b
#     b = c
#     i += 1
# 
# print(i)
