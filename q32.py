#!/usr/bin/python

# Problem 32

# We shall say that an n-digit number is pandigital if it makes use of 
# all the digits 1 to n exactly once; for example, the 5-digit number, 
# 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product 
# identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to 
# only include it once in your sum.

from itertools import permutations as p

def pdi( _digits, _f1length, _f2length ):
    
    "get pandigital identities, for pandigitals with digits in _digits, and f1*f2=product f1 has length _f1length and f2 has length _f2length"

    products = {}
    factors1 = p( _digits, _f1length ) # two-digit factors

    # find all 1..9 pandigital identites with lengths 2*3=4
    for f in factors1:
        rd = [ d for d in digits if d not in f ] # remaining digits
        factors2 = p( rd, _f2length ) # two-digit factors
        for F in factors2:
            rd2 = [ d for d in rd if d not in f and d not in F ] # remaining digits available for product
            possible_products = p( rd2, len(_digits)-_f1length-_f2length )
            for P in possible_products:

                #convert factors and product from lists to ints
                factor1 = int( "".join( map(str,f) ) )
                factor2 = int( "".join( map(str,F) ) )
                product = int( "".join( map(str,P) ) )

                if factor1*factor2==product:
                    products[ product ] = (factor1,factor2)
                    print( "%d * %d = %d" % ( factor1,factor2,product ))

    return products

   

if __name__ == "__main__":

    digits = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

    p23 = pdi( digits, 2, 3)
    p14 = pdi( digits, 1, 4)

    print( "sum of products: %d" % ( sum( p23.keys() ) + sum( p14.keys() ) ) )
