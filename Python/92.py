#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     04/05/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
tottimes = 0
i = 1
runtimes = 0

def square(a):
    sqlist = []
    for i in a:
        sqlist.append(i**2)
    ret = sqlist[0]
    print(ret)
    return ret

while i < 5:
    isplit = [int(i) for i in str(i)]
    binary = 1
    i1 = i
    print(i)
    print(isplit)
    while isplit != [1]:
        binary = 0
        isplit = [int(i) for i in str(i1)]
        if isplit == [1]:
            tottimes += 1
            i += 1
            break
        if isplit == [89]:
            tottimes += 1
            i += 1
            break
        i1 = square(isplit)
    while binary == 1:
        if runtimes >= 1:
            break
        while isplit != [89]:
            if isplit != [1]:
                isplit = [int(i) for i in str(i1)]
                if isplit == [1]:
                    tottimes += 1
                    i += 1
                    break
                if isplit == [89]:
                    tottimes += 1
                    i += 1
                    break
                i1 = square(isplit)
            else:
                i += 1
                runtimes += 1
                break


print(tottimes)




















