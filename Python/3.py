#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     09/02/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
factorlist = []
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



for i in range(1, 775147):
    if 600851475143%i == 0:
        if is_prime(i) == True:
            factorlist.append(i)

print(max(factorlist))







