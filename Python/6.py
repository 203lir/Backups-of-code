#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Haihong
#
# Created:     03/11/2017
# Copyright:   (c) Haihong 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
firstnums = []
amount = 0
while amount <= 100:
    firstnums.append (amount)
    amount += 1
print (firstnums)
#-------------------------------------------------------------------------------
total = 0
for n in range(1,101):
    y = n**2
    total += y
summ = 0
for i in range (1, 101):
    summ += i
sq = summ**2

print (sq-total)