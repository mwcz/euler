#!/usr/bin/python

# Problem 4

# A palindromic number reads the same both ways. The 
# largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 * 99.
# 
# Find the largest palindrome made from the product 
# of two 3-digit numbers.

def is_pdrome( _s ):

    if len( _s ) in (0,1): 
        return True

    if _s[0] == _s[ len(_s) - 1 ]: 
        return is_pdrome( _s[ 1 : len(_s) - 1 ] )

    return False

def find_pdrome( _digs ):

    nums = range( 10**(_digs-1), 10**_digs )
    nums.reverse()

    max = [0,0,0]

    for n in nums:
        for m in nums:
            o = n * m
            if is_pdrome( str( o ) ):
                if o > max[2]:
                    max[0] = n
                    max[1] = m
                    max[2] = o

    print( max )

find_pdrome( 3 )
