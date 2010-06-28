#!/usr/bin/python

# Problem 5

# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any 
# remainder.
# 
# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 
# to 20?


# hmm, to be divisible by 1..20, the number must
# have prime factors of:
#
#   2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19
#
# oops, I solved it without writing a program :)

answer = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

print( answer )
