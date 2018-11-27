#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Haihong
#
# Created:     09/02/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
primelist = []
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

for i in range(1, 1000003):
    if is_prime(i) == True:
        primelist.append(i)

end = primelist[10000]
print(end)