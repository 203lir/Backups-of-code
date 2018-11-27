#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     29/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
total = 0

for i in range(1, 60):
    for i1 in range(1, 60):
        x = i**i1
        xstr = str(x)
        length = len(xstr)
        if length == i1:
            total += 1
            print(i, i1, x)

print(total)
