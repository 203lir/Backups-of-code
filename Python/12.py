#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     18/06/2020
# Copyright:   (c) No 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def factors(tobefactored):
    numoffactors = 0
    top = math.ceil(math.sqrt(tobefactored))
    for i in range (1, top):
        if tobefactored%i == 0:
            numoffactors += 1
    numoffactors *= 2
    if math.sqrt(tobefactored)%1 == 0:
        numoffactors += 1
    return numoffactors

trianglenum = 0
addtotrianglenum = 1
stop = False

while stop == False:
    trianglenum += addtotrianglenum
    addtotrianglenum += 1
    if factors(trianglenum) > 500:
        print(trianglenum)
        stop = True







