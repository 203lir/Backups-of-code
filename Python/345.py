#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     27/04/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
tot = 0
rowlist = []
collist = []

matrix = [[7, 53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],
[627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
[447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
[217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
[960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
[870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
[973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
[322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
[445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
[414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
[184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
[821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
[ 34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
[815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
[813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]]

for row1 in range(1, 16):
    for row2 in range(1, 16):
        for row3 in range(1, 16):
            for row4 in range(1, 16):
                for row5 in range(1, 16):
                    for row6 in range(1, 16):
                        for row7 in range(1, 16):
                            for row8 in range(1, 16):
                                for row9 in range(1, 16):
                                    for row10 in range(1, 16):
                                        for row11 in range(1, 16):
                                            for row12 in range(1, 16):
                                                for row13 in range(1, 16):
                                                    for row14 in range(1, 16):
                                                        for row15 in range(1, 16):
                                                            for col1 in range(1, 16):
                                                                for col2 in range(1, 16):
                                                                    for col3 in range(1, 16):
                                                                        for col4 in range(1, 16):
                                                                            for col5 in range(1, 16):
                                                                                for col6 in range(1, 16):
                                                                                    for col7 in range(1, 16):
                                                                                        for col8 in range(1, 16):
                                                                                            for col9 in range(1, 16):
                                                                                                for col10 in range(1, 16):
                                                                                                    for col11 in range(1, 16):
                                                                                                        for col12 in range(1, 16):
                                                                                                            for col13 in range(1, 16):
                                                                                                                for col14 in range(1, 16):
                                                                                                                    for col15 in range(1, 16):
                                                                                                                        rowlist.append(row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15)
                                                                                                                        collist.append(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15)
                                                                                                                        row = set(rowlist)
                                                                                                                        col = set(collist)
                                                                                                                        rowlist.sort()
                                                                                                                        collist.sort()
                                                                                                                        row.sort()
                                                                                                                        col.sort()
                                                                                                                        if rowlist == row:
                                                                                                                            print(1)
                                                                                                                        else:
                                                                                                                            break
                                                                                                                        if collist == col:
                                                                                                                            print(2)
                                                                                                                        else:
                                                                                                                            break
                                                                                                                        num1 = matrix[row1][col1]
                                                                                                                        num2 = matrix[row2][col2]
                                                                                                                        num3 = matrix[row3][col3]
                                                                                                                        num4 = matrix[row4][col4]
                                                                                                                        num5 = matrix[row5][col5]
                                                                                                                        num6 = matrix[row6][col6]
                                                                                                                        num7 = matrix[row7][col7]
                                                                                                                        num8 = matrix[row8][col8]
                                                                                                                        num9 = matrix[row9][col9]
                                                                                                                        num10 = matrix[row10][col10]
                                                                                                                        num11 = matrix[row11][col11]
                                                                                                                        num12 = matrix[row12][col12]
                                                                                                                        num13 = matrix[row13][col13]
                                                                                                                        num14 = matrix[row14][col14]
                                                                                                                        num15 = matrix[row15][col15]
                                                                                                                        if num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15 > tot:
                                                                                                                            tot += num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11+num12+num13+num14+num15



















