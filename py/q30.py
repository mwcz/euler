#!/usr/bin/python

# Problem 30

# Surprisingly there are only three numbers that can be written as the sum 
# of fourth powers of their digits:
# 
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
# 
# As 1 = 1^4 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

if __name__ == "__main__":

    # the largest number POSSIBLE number is 77777.
    # 5*7^5 = 84035, which is too high but close enough
    # to serve as a max

    max = 999999
    total_sum = 0

    for i in xrange(2,max+1):
        num_string = str( i )
        sum_of_fifth_powers = 0
        for digit in num_string:
            sum_of_fifth_powers += int(digit)**5
        if i == sum_of_fifth_powers:
            total_sum += sum_of_fifth_powers
            print( i, sum_of_fifth_powers )

    print( "total sum = %d" % total_sum )
