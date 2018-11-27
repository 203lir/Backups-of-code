#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     03/10/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
numlist = []
currentlist = []
numberthing = 0
resultlist = []
resultlist1 = []

for i in range(1, 1001):
    append = 1/i
    numlist.append(append)

print(numlist)

for x in range(0, 10):
    hi = numlist[x]
    strhi = str(hi)
    for y in strhi:
        currentlist.append(y)
    del currentlist[0]
    del currentlist[0]
    print(currentlist)
    for z in currentlist:
        for thing in range(0, len(currentlist)-numberthing-2):
            if z == currentlist[thing]:
                if currentlist[numberthing] == currentlist[thing + 1]:
                    if currentlist[numberthing + 1] == currentlist[thing + 2]:
                        result = thing+1-numberthing
                        resultlist.append(result)
                        resultlist1.append(x)
        numberthing += 1

hi1 = max(resultlist)
print(hi1)
hi2 = resultlist.index(hi1)
print(hi2)
hi3 = resultlist1[hi2]
print(hi3)
print(resultlist)
print(resultlist1)











