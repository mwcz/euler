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

from json import loads

# Right now, this solution is ridiculously stupid and doesn't work
# At All.

coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
coins.reverse()

ANSWERS = {}

def ways( n, c=[] ):

    if n == 0: 
        c.reverse()
        #print(int("".join(map( str, c ))))
        ANSWERS[ str(c) ] = 0
        c = []
        return 0
    if n  < 0: return 0
    
    running_sum = 0

    for coin in coins:
        if coin <= n:
            c.append(coin)
            running_sum += ways( n - coin, c )

    return running_sum

if __name__ == "__main__":
    
    want = 10

    ways(want)

    total = 0
    running_sum = 0
    all_combos = loads(ANSWERS.keys()[len(ANSWERS)-1])
    for n in all_combos:
        running_sum += n
        if running_sum == want:
            running_sum = 0
            total += 1
        elif running_sum > want:
            print("WOAH")
            break

    print( total )
        

