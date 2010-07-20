#!/usr/bin/python

# Problem 35

# The number, 197, is called a circular prime because all 
# rotations of the digits: 197, 971, and 719, are themselves 
# prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
# 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from gmpy import next_prime, is_prime

def rotate( _s ):

    # coerce to string
    _s = str( _s )

    s = [ c for c in _s ]

    s.append( s.pop(0) )

    return "".join( [ c for c in s ] )

def rotations( _s ):

    # coerce to string
    _s = str( _s )

    rots = [ _s ]

    for i in xrange( len( _s ) - 1 ):
        rots.append( rotate( rots[-1] ) )

    return rots

if __name__ == "__main__":

    p = 2

    circular_primes = []

    # for all primes below 1e6
    while p < 1000000:

        is_circular = True

        p_rotations = rotations( p )

        for r in p_rotations:

            if not is_prime( int(r) ):
                is_circular = False
                break

        if is_circular:
            circular_primes.append( p_rotations )
                
        p = next_prime( p )

    print( len( circular_primes ) )
