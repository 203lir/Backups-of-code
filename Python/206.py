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
square = 0
for i in range (1000000000, 5000000000):
    squared = square ** 2
    alist = list(str(squared))
    a = (alist [0])
    if a == 1:
        b = (alist [2])
        if b == 2:
            c = (alist [4])
            if c == 3:
                d = (alist [6])
                if d == 4:
                    e = (alist [8])
                    if e == 5:
                        f = (alist [10])
                        if f == 6:
                            g = (alist [12])
                            if g == 7:
                                h = (alist [14])
                                if h == 8:
                                    j = (alist [16])
                                    if j == 9:
                                        k = (alist [18])
                                        if k == 0:
                                            print (squared)

