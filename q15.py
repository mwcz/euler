#!/usr/bin/python

# Problem 15

# Starting in the top left corner of a 2x2 grid, there are 6 
# routes (without backtracking) to the bottom right corner.
# 
#     (img) http://projecteuler.net/project/images/p_015.gif
# 
# How many routes are there through a 20x20 grid?

# can be solved by the combinatorics equation (x+y)! / (x!y!)
# in this case, 40 choose 20, or 40! / (20!*20!)

GRID_SIZE = (20,20)

GRIDS = {}

for x in xrange( GRID_SIZE[0]+1 ):
    GRIDS[x]={}
    for y in xrange( GRID_SIZE[1]+1 ):
        GRIDS[x][y]=0

def num_paths( (x, y) ):
    "recursive function for finding the number of paths through an (x,y)  grid."

    if GRIDS[x][y] != 0:
        return GRIDS[x][y]

    if x == 0:
        return 1
    if y == 0:
        return 1

    c = num_paths( (x-1,y) ) + num_paths( (x,y-1) )
    GRIDS[x][y] = c

    return c

print( num_paths( GRID_SIZE ) )
