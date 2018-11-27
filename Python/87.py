#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     01/06/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
total = 0

def check (b):
    hi = 0
    while hi == 0:
        for check1 in range (1, 7072):
            for check2 in range(1, 7072):
                for check3 in range(1, 7072):
                    if is_prime(check1) == False:
                        hi = 1
                    if is_prime(check2) == False:
                        hi = 1
                    if is_prime(check3) == False:
                        hi = 1
                    if check1 ** 2 + check2 ** 3 + check3 ** 4 == b:
                        return True


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


for i in range (1, 50000000):
    if check(i):
        total += 1
        print(total)

print(total)




















