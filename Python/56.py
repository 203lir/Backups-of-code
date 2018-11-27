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
sumlist = []
for i in range(1, 100):
    for x in range(1, 100):
        y = i**x
        digitsnum = math.log(y)
        digitsnum //= 1
