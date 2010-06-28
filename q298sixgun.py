#!/usr/bin/python

import os

os.chdir( "/home/mwc/workspace/random/euler/" )
f = file( "/home/mwc/workspace/random/euler/SCORES" )

while True:
    os.system("./q298.py >> SCORES")    

