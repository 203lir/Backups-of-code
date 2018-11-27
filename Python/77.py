#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     23/03/2018
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

primelist = [0]
for i in range(1, 25000000):
    if is_prime(i):
        primelist.append(i)

primec = 0

while primec < 5001:
    for i in range(100, 100000000):
        for i1 in range(1, 10000):
            if primec[i1] <= i:
                i3 = i1
                i1 = 1000000
        for i2 in range(1, i3):
            for i4 in range(1, i3):
                for i5 in range(1, i3):
                    for i6 in range(1, 13):
                        i2thing = primelist[i2]
                        i4thing = primelist[i4]
                        i5thing = primelist[i5]
                        i6thing = primelist[i6]
                        if i2thing + i4thing + i5thing + i6thing == i:
                            primec += 1
        for i7 in range(1, 100000):
            for i8 in range(1, i3):
                i8thing = primelist[i8]
                if i7*i8thing == i:
                    primec += 1




        if primec > 5000:
            print(i)
        primec = 0










