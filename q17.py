#!/usr/bin/python

# Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, 
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
# out in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
# and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in 
# compliance with British usage.

digs = {  0: "",
          1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         14: "fourteen",
         15: "fifteen",
         16: "sixteen",
         17: "seventeen",
         18: "eighteen",
         19: "nineteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety",
         }

def letters( n ):
    "convert any number 1..1000 from digits into words."
    if len(str(n)) == 4: # number is 1000
        return "onethousand"
    if len(str(n)) == 3: # number is 100..999
        word = digs[n/100] + "hundred"
        # now figure out if stupid "and" should be included
        rest = letters( n%100 )  # len("hundred") == 7
        if len(rest): # if the rest of the number is not just zeroes we need an "and"
            word += "and"
        word += rest
        return word
    if len(str(n)) == 2: # number is 10..99
        if digs.has_key(n): # this will be true if the number is 11..19 or a multiple of 10
            return digs[n]
        else:
            return digs[ n - n%10 ] + digs[ n%10 ] # get the name for the tens place, then the name for the ones place
    if len(str(n)) == 1: # number is 1..9
        return digs[n]

print( sum( [len(letters(i)) for i in range(1,1001)]  ) )

