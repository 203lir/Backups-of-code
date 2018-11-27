#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     11/05/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib.request


def romnuminterp(romnum):
    total = 0
    i = 0
    while i != 1:
        i = 1
        if "IV" in romnum:
            total += 4
            romlist = list(romnum)
            romlist.remove("I")
            romlist.remove("V")
            romnum = ''.join(romlist)
            i = 0
        if "IX" in romnum:
            total += 9
            romlist = list(romnum)
            romlist.remove("I")
            romlist.remove("X")
            romnum = ''.join(romlist)
            i = 0
        if "XL" in romnum:
            total += 40
            romlist = list(romnum)
            romlist.remove("X")
            romlist.remove("L")
            romnum = ''.join(romlist)
            i = 0
        if "XC" in romnum:
            total += 90
            romlist = list(romnum)
            romlist.remove("X")
            romlist.remove("C")
            romnum = ''.join(romlist)
            i = 0
        if "CD" in romnum:
            total += 400
            romlist = list(romnum)
            romlist.remove("C")
            romlist.remove("D")
            romnum = ''.join(romlist)
            i = 0
        if "CM" in romnum:
            total += 900
            romlist = list(romnum)
            romlist.remove("C")
            romlist.remove("M")
            romnum = ''.join(romlist)
            i = 0
        if "I" in romnum:
            total += 1
            romlist = list(romnum)
            romlist.remove("I")
            romnum = ''.join(romlist)
            i = 0
        if "V" in romnum:
            total += 5
            romlist = list(romnum)
            romlist.remove("V")
            romnum = ''.join(romlist)
            i = 0
        if "X" in romnum:
            total += 10
            romlist = list(romnum)
            romlist.remove("X")
            romnum = ''.join(romlist)
            i = 0
        if "L" in romnum:
            total += 50
            romlist = list(romnum)
            romlist.remove("L")
            romnum = ''.join(romlist)
            i = 0
        if "C" in romnum:
            total += 100
            romlist = list(romnum)
            romlist.remove("C")
            romnum = ''.join(romlist)
            i = 0
        if "D" in romnum:
            total += 500
            romlist = list(romnum)
            romlist.remove("D")
            romnum = ''.join(romlist)
            i = 0
        if "M" in romnum:
            total += 1000
            romlist = list(romnum)
            romlist.remove("M")
            romnum = ''.join(romlist)
            i = 0
    return total



romnuminterplist = []
romnumopen = urllib.request.urlopen('https://projecteuler.net/project/resources/p089_roman.txt')
romnumread = romnumopen.read()
romnumstr = str(romnumread)
romnumspace = romnumstr.replace("n", " ")
romnumlist = romnumspace.split()
for i in romnumlist:
    romnuminterplist.append(romnuminterp(i))




def romnumcreate(num):
    romnum = []
    i1 = 0
    while i1 != 1:
        i1 = 1
        if num >= 1000:
            romnum.append("M")
            num -= 1000
            i1 = 0
        if num >= 900:
            if num < 1000:
                romnum.append("CM")
                num -= 900
                i1 = 0
        if num >= 500:
            if num < 900:
                romnum.append("D")
                num -= 500
                i1 = 0
        if num >= 400:
            if num < 500:
                romnum.append("CD")
                num -= 400
                i1 = 0
        if num >= 100:
            if num < 400:
                romnum.append("C")
                num -= 100
                i1 = 0
        if num >= 90:
            if num < 100:
                romnum.append("XC")
                num -= 90
                i1 = 0
        if num >= 50:
            if num < 90:
                romnum.append("L")
                num -= 50
                i1 = 0
        if num >= 40:
            if num < 50:
                romnum.append("XL")
                num -= 40
                i1 = 0
        if num >= 10:
            if num < 40:
                romnum.append("X")
                num -= 10
                i1 = 0
        if num >= 9:
            if num < 10:
                romnum.append("IX")
                num -= 9
                i1 = 0
        if num >= 5:
            if num < 9:
                romnum.append("V")
                num -= 5
                i1 = 0
        if num >= 4:
            if num < 5:
                romnum.append("IV")
                num -= 4
                i1 = 0
        if num >= 1:
            if num < 4:
                romnum.append("I")
                num -= 1
                i1 = 0
    romnumjoined = ''.join(romnum)
    return romnumjoined

totfinal = 0

newromnumlist = []
for i1 in romnuminterplist:
    newromnumlist.append(romnumcreate(i1))
for i in range (0, 1000):
    hi = romnumlist[i]
    hi1 = newromnumlist[i]

    m1 = hi.count("M")
    d1 = hi.count("D")
    c1 = hi.count("C")
    l1 = hi.count("L")
    x1 = hi.count("X")
    v1 = hi.count("V")
    i1 = hi.count("I")
    tot1 = m1+d1+c1+l1+x1+v1+i1

    m2 = hi1.count("M")
    d2 = hi1.count("D")
    c2 = hi1.count("C")
    l2 = hi1.count("L")
    x2 = hi1.count("X")
    v2 = hi1.count("V")
    i2 = hi1.count("I")
    tot2 = m2+d2+c2+l2+x2+v2+i2

    diff = tot2 - tot1
    totfinal += diff
    print(diff)
    print(hi, hi1)


print(totfinal)










