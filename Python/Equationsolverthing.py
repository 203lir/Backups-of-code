#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     17/10/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def equationsolver (somelist):
    alist = []
    alist2 = []
    aninteger = 0
    total1 = 0
    total2 = 0
    for i in somelist:
        if aninteger == 0:
            if i == "=":
                aninteger = 1
        if aninteger == 0:
            alist.append(i)
        if aninteger == 2:
            alist2.append(i)
        if aninteger == 1:
            aninteger = 2
    print(alist)
    print(alist2)
    total1 = equationmath(alist)
    total2 = equationmath(alist2)
    print(total1)
    print(total2)


def equationmath (alist):
    anotherinteger = 0
    total = 0
    for i in range(1, 50):
        for i in alist:
            if i == "^":
                int1 = int(alist[anotherinteger-1])
                int2 = int(alist[anotherinteger+1])
                if int1 != "x":
                    if int2 != "x":
                        total += int1 ** int2
            if i == "*":
                int1 = alist[anotherinteger-1]
                int2 = alist[anotherinteger+1]
                if int1 != "x":
                    if int2 != "x":
                        total += int1 * int2
            if i == "/":
                int1 = alist[anotherinteger-1]
                int2 = alist[anotherinteger+1]
                if int1 != "x":
                    if int2 != "x":
                        total += int1 / int2
            if i == "+":
                int1 = alist[anotherinteger-1]
                int2 = alist[anotherinteger+1]
                if int1 != "x":
                    if int2 != "x":
                        total += int1 + int2
            if i == "-":
                int1 = alist[anotherinteger-1]
                int2 = alist[anotherinteger+1]
                if int1 != "x":
                    if int2 != "x":
                        total += int1 - int2
            anotherinteger += 1

inpt = input("Enter some form of some kind of equation thing with a space between each symbol/number, and where the only variable is defined as x.")
print("Here's what you entered: ", inpt)
inptlist = inpt.split()
print(inptlist)
equationsolver(inptlist)















