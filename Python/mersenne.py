#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     26/01/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

start = time.time()

ifh = 0

for d in range(1, 1001):

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

    x = 2
    for i in range (1, 50):
        y = 2 ** x
        n = y-1
        if is_prime(n) == True:
            ifh += 1

        x += 1

    n = 0
    n += 1

end = time.time()

tottime = end - start
avtime = tottime

print(avtime)