#!/usr/bin/python

# Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which 
# is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

from gmpy import gcd
from operator import mul

def badfrac( _n, _d ):
    
    "returns true if n/d can be reduced by incorrectly cancelling digits in the numerator and denominator. returns false otherwise, or if it is a trivial example, like 30/50"

    n = [ c for c in str(_n) ]
    d = [ c for c in str(_d) ]

    # eliminate trivial examples
    if _n % 10 == 0 and _d % 10 == 0 : return False

    ratio = float( _n ) / float( _d )

    common_digits = False

    # cancel all common digits
    for nd in n:
        if nd in d:
            common_digits = True
            n.remove(nd)
            d.remove(nd)

    if not common_digits: return False

    n_number = int( "".join( [ c for c in n ] ) )
    d_number = int( "".join( [ c for c in d ] ) )

    if d_number == 0: return False

    return True if float( n_number ) / float( d_number ) == ratio else False

if __name__ == "__main__":

    numers = []
    denoms = []

    for numer in range(10,100):
        for denom in range(numer+1,100):
            if badfrac( numer, denom ):
                numers.append(numer)
                denoms.append(denom)

    numer = reduce( mul, numers )
    denom = reduce( mul, denoms )

    divisor = gcd( numer, denom )

    print( denom / divisor )
