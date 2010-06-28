#!/usr/bin/python

# Problem 7

# By listing the first six prime numbers: 
# 
#     2, 3, 5, 7, 11, and 13
# 
# We can see that the 6th prime is 13.
# 
# What is the 10001st prime number?

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
    if is_prime:
        p.append(poss_prime)
    if len(p) >= 10001:
        break

print(p)
