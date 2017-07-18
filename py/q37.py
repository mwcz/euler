#!/usr/bin/python

# Problem 37

# The number 3797 has an interesting property. Being prime itself, it 
# is possible to continuously remove digits from left to right, and 
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can 
# work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable 
# from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from gmpy import next_prime, is_prime

def truncatable( _s ):

    s = str(_s)
    l = len(s)

    for i in range(l):
        if not is_prime( int(s[i:]) ):
            return False
        if not is_prime( int(s[:i+1]) ):
            return False

    return True

if __name__ == "__main__":

    primes = []

    p = 7

    while len(primes) < 11:
        p = next_prime(p)
        if truncatable( p ): primes.append(p)
        
    print(sum(primes))
