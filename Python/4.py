#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     16/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
plist = []

def pcheck(x):
    xlist = list(str(x))
    ylist = list(str(x))
    xlist.reverse()
    if ylist == xlist:
        return True
    else:
        return False


for i1 in range(100, 1000):
    for i2 in range(100, 1000):
        tot = i1*i2
        if pcheck(tot):
            plist.append(tot)

print(max(plist))








