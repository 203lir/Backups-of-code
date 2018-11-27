#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     16/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
list = []
x = 0

matrix = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

for i in range(1, 16384):
    for x in range(-1, 1):
        for x1 in range(-1, 1):
            for x2 in range(-1, 1):
                for x3 in range(-1, 1):
                    for x4 in range(-1, 1):
                        for x5 in range(-1, 1):
                            for x6 in range(-1, 1):
                                for x7 in range(-1, 1):
                                    for x8 in range(-1, 1):
                                        for x9 in range(-1, 1):
                                            for x10 in range(-1, 1):
                                                for x11 in range(-1, 1):
                                                    for x12 in range(-1, 1):
                                                        for x13 in range(-1, 1):
                                                            y = 0
                                                            num1 = [0][y]
                                                            y += x
                                                            if y < 0:
                                                                y = 0
                                                            num2 = [1][y]
                                                            y += x1
                                                            if y < 0:
                                                                y = 0
                                                            num3 = [2][y]
                                                            y += x2
                                                            if y < 0:
                                                                y = 0
                                                            num4 = [3][y]
                                                            y += x3
                                                            if y < 0:
                                                                y = 0
                                                            num5 = [4][y]
                                                            y += x4
                                                            if y < 0:
                                                                y = 0
                                                            num6 = [5][y]
                                                            y += x5
                                                            if y < 0:
                                                                y = 0
                                                            num7 = [6][y]
                                                            y += x6
                                                            if y < 0:
                                                                y = 0
                                                            num8 = [7][y]
                                                            y += x7
                                                            if y < 0:
                                                                y = 0
                                                            num9 = [8][y]
                                                            y += x8
                                                            if y < 0:
                                                                y = 0
                                                            num10 = [9][y]
                                                            y += x9
                                                            if y < 0:
                                                                y = 0
                                                            num11 = [10][y]
                                                            y += x10
                                                            if y < 0:
                                                                y = 0
                                                            num12 = [11][y]
                                                            y += x11
                                                            if y < 0:
                                                                y = 0
                                                            num13 = [12][y]
                                                            y += x12
                                                            if y < 0:
                                                                y = 0
                                                            num14 = [13][y]
                                                            y += x13
                                                            if y < 0:
                                                                y = 0
                                                            num15 = [14][y]
                                                            if y < 0:
                                                                y = 0
                                                            tot = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15
                                                            list.append(tot)
print(max(list))







