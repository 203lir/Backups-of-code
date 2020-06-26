#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     09/04/2020
# Copyright:   (c) No 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
capvalues = [[], []]
no = True

def parallelcaps (n, m):
    total = n+m
    return float(total)

def seriescaps (n, m):
    hi = 0
    hi += 1/n
    hi += 1/m
    return float(1/hi)

def init():
    capvalues[0].append(1)
    capvalues[1].append(float(100))
    for i in range (2, 19):
        capvalues[0].append(i)
        capvalues[0].append(i)
        capvalues[1].append(float(100*i))
        capvalues[1].append(100/i)

init()

for i in range (3, 19):
    for a in capvalues[0]:
        if a < i:
            for b in capvalues[0]:
                if a+b == i:
                    parallel = parallelcaps(capvalues[1][a], capvalues[1][b])
                    if parallel not in capvalues[1]:
                        capvalues[0].append(i)
                        capvalues[1].append(parallel)
                    series = seriescaps(capvalues[1][a], capvalues[1][b])
                    if series not in capvalues[1]:
                        capvalues[0].append(i)
                        capvalues[1].append(series)

print(capvalues[0])





