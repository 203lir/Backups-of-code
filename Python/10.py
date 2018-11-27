#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Haihong
#
# Created:     01/12/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
prime = 0
total = 0

def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False

        sq = int(n**0.5)
        f = 5

        while f <= sq:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f += 6
        return True

while prime < 2000000:
    if is_prime(prime):
        total += prime
    prime += 1

print(total)










