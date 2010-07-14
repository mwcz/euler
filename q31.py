#!/usr/bin/python

# Problem 31

# In England the currency is made up of pound, L, and pence, p, and 
# there are eight coins in general circulation:
# 
#     1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
# 
# It is possible to make L2 in the following way:
# 
#     1L1 + 150p + 220p + 15p + 12p + 31p
# 
# How many different ways can L2 be made using any number of coins?

coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]

def ways( n, c ):

    "n is the quantity we want to match.  c is the previously chosen coin."

    if n == 0: return 1 # if we hit the mark, count it as 1 solution
    if n <= 0: return 0 # if we overshot and spent too much, no solution

    # get every coin that is less than or equal to n (the remaining amount
    # of money), and greater than or equal to c (the last coin we used).
    # c exists so that we don't wind up with duplicate solutions like 
    # (1,2,2) and (2,2,1) for 5pence.
    possibilities = [ coin for coin in coins if coin <= n and coin >= c ]
    count = 0

    for coin in possibilities:
        count += ways( n - coin, coin )

    return count

if __name__ == "__main__":
    
    print( ways( 200, 0 ) )
