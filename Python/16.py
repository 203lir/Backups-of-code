#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     03/11/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
x = 2**1000
n = str(x)
total = 0
for i in n:
    i = int(i)
    total += i
print(total)