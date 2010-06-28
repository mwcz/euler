#!/usr/bin/python

# Problem 298

# Larry and Robin play a memory game involving of a sequence of random numbers between 1 and 10, inclusive, that are called out one at a time. Each player can remember up to 5 previous numbers. When the called number is in a player's memory, that player is awarded a point. If it's not, the player adds the called number to his memory, removing another number if his memory is full.
# 
# Both players start with empty memories. Both players always add new missed numbers to their memory but use a different strategy in deciding which number to remove:
# Larry's strategy is to remove the number that hasn't been called in the longest time.
# Robin's strategy is to remove the number that's been in the memory the longest time.
# 
# Example game:
# Turn    Called
# number  Larry's
# memory  Larry's
# score   Robin's
# memory  Robin's
# score
# 1   1   1   0   1   0
# 2   2   1,2 0   1,2 0
# 3   4   1,2,4   0   1,2,4   0
# 4   6   1,2,4,6 0   1,2,4,6 0
# 5   1   1,2,4,6 1   1,2,4,6 1
# 6   8   1,2,4,6,8   1   1,2,4,6,8   1
# 7   10  1,4,6,8,10  1   2,4,6,8,10  1
# 8   2   1,2,6,8,10  1   2,4,6,8,10  2
# 9   4   1,2,4,8,10  1   2,4,6,8,10  3
# 10  1   1,2,4,8,10  2   1,4,6,8,10  3
# Denoting Larry's score by L and Robin's score by R, what is the expected value of |L-R| after 50 turns? Give your answer rounded to eight decimal places using the format x.xxxxxxxx .

from random import randrange as r

f = file( "/home/mwc/workspace/random/euler/ITERS", "w" )

count = 0
PRE = 0.0
AVG = 0.0

while True:
    count += 1

    P1 = []
    P2 = []

    P1S = 0
    P2S = 0

    for turn in xrange(1,51):

        # random number
        number = r(1,11)

        #print( "%d, r = %d" % ( turn, number ) )

        # if empty lists, add first number
        if len( P1 ) == 0:
            P1.append( number )
            P2.append( number )

        # Larry's strategy is to remove the number that hasn't been called in the longest time.
        if number in P1:
            P1S += 1
            P1.pop( P1.index( number ) )
            P1.append( number )
        else:
            if len( P1 ) == 5:
                P1.pop( 0 )
            P1.append( number )

        # Robin's strategy is to remove the number that's been in the memory the longest time.
        if number in P2:
            P2S += 1
        else:
            if len( P2 ) == 5:
                P2.pop( 0 )
            P2.append( number )

    PRE += abs( P1S - P2S )

    # print average every 524288 iterations
    if count == 4096:
        AVG += PRE / 4096
        AVG /= 2
        PRE = 0.0
        print( AVG )
        f.write( "%f\n" % ( AVG ) )
        f.flush()
        count = 0
