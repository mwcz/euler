#!/usr/bin/python

# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


p = [2]

count = 1
poss_prime = p[len(p)-1] + 1

while True:
    last_prime = p[len(p)-1]
    poss_prime += 1
    is_prime = True
    for prime in p:
        if poss_prime % prime == 0:
            is_prime = False
            break
    if poss_prime > 2e6:
        break
    if is_prime:
        p.append(poss_prime)

print( reduce( lambda a,b:a+b, p ) )
