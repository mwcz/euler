#!/usr/bin/python

# Problem 15

# Starting in the top left corner of a 2x2 grid, there are 6 
# routes (without backtracking) to the bottom right corner.
# 
#     (img) http://projecteuler.net/project/images/p_015.gif
# 
# How many routes are there through a 20x20 grid?

GRID_SIZE = (3,3)

def num_paths( (x, y), c=0 ):
    "recursive function for finding the number of paths through a grid.  x and y are 'remaining x' and 'remaining y' and c is the count"

    if x == 0: return c + y
    if y == 0: return c + x

    c += num_paths( (x-1,y), c+1 )
    c += num_paths( (x,y-1), c+1 )

    return c

print( num_paths( GRID_SIZE ) )
