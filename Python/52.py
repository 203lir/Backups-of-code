#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     09/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for i1 in range(1, 100000000):
    i2 = i1*2
    i3 = i1*3
    i4 = i1*4
    i5 = i1*5
    i6 = i1*6
    istr1 = str(i1)
    istr2 = str(i2)
    istr3 = str(i3)
    istr4 = str(i4)
    istr5 = str(i5)
    istr6 = str(i6)
    i1list = []
    i2list = []
    i3list = []
    i4list = []
    i5list = []
    i6list = []
    for x1 in istr1:
        i1list.append(x1)
    for x2 in istr2:
        i2list.append(x2)
    for x3 in istr3:
        i3list.append(x3)
    for x4 in istr4:
        i4list.append(x4)
    for x5 in istr5:
        i5list.append(x5)
    for x6 in istr6:
        i6list.append(x6)
    i1list.sort()
    i2list.sort()
    i3list.sort()
    i4list.sort()
    i5list.sort()
    i6list.sort()
    if i1list == i2list:
        if i1list == i3list:
            if i1list == i4list:
                if i1list == i5list:
                    if i1list == i6list:
                        print(i1)



