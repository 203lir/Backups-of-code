#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Haihong
#
# Created:     01/12/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
x = 9999999999
sum_ = 1
for x in range (1, 10000000000):
    sum_ *= x
    x -= 1
print (sum_)

print (sum(map(int, str(sum_))))