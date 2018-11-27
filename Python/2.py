#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     15/12/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

total = 0
cachenum2 = 1
cachenum = 1
for i in range (0, 500):
    cachenum += cachenum2
    cachenum2 += cachenum
    if cachenum < 4000001:
        if cachenum % 2 == 0:
            total += cachenum
            print(cachenum)
            print(total)
    if cachenum2 < 4000001:
        if cachenum2 % 2 == 0:
            total += cachenum2
            print(cachenum2)
            print(total)
print(total)