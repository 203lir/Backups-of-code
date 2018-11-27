#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     09/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
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

def hi(x, y, i):
    tot = x+y
    if i == tot:
        return True
    else:
        return False

numlist = [1, 2, 3]
worklist = []

for i1 in range(2, 1000000):
    check = i1 * 2 + 1
    if is_prime(check) == False:
        for i2 in range(2, 100000):
            if is_prime(i2):
                for i3 in range(1, 1000):
                    i4 = i3 ** 2
                    i5 = i4*2
                    if hi(i2, i5, check) == False:
                        numlist.append(check)
                    else:
                        worklist.append(check)
                    x = len(numlist)
                    num1 = numlist[x-1]
                    num2 = numlist[x-2]
                    if num1 != num2:
                        bob = numlist[x-1]
                        if bob not in worklist:
                            print(bob)












