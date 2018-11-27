#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     27/10/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#squarelist = []
#y = 0
#for i in range (1, 20):
    #z = y*y
    #squarelist.append(z)
    #y += 1
#print(squarelist)
#-------------------------------------------------------------------------------
#cubelist = []
#a = 0
#for i in range (1, 20):
    #b = a*a*a
    #cubelist.append(b)
    #a += 1
#print(cubelist)
#-------------------------------------------------------------------------------
palinlist = []
x = 1
for i in range (1, 6000):
    xstr = str(x)
    xint = int(xstr[::-1])
    if x == xint:
        palinlist.append(x)
    x += 1
print (palinlist)
#-------------------------------------------------------------------------------
palinamount = 0
palinadd = []
while palinamount < 6:
    for square in range (1, 300):
        squared = square ** 2
        for cube in range (1, 300):
            cubed = cube ** 3
            total = squared + cubed
            if total in palinlist:
                palinadd.append(total)
                palinamount += 1
palinadd.sort()
print (palinadd)
#-------------------------------------------------------------------------------