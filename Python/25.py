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
import math

fiblist = []

working = 1
working1 = 1
final = 1

for i in range(2, 10000):
    x = list(str(final))
    if len(x) >= 1000:
        fiblist.append(i)

    final = working + working1
    working = working1
    working1 = final

fiblist.sort()
print(fiblist[0])






