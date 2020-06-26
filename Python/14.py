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


def collatz(collatzed):
    if collatzed%2 == 0:
        return collatzed/2
    else:
        return (3*collatzed)+1

maxchainlength = [0, 0]

for i in range (1, 1000000):
    nextnuminchain = i
    chainlength = 0
    currentnuminchain = i
    while nextnuminchain != 1:
        nextnuminchain = collatz(currentnuminchain)
        chainlength += 1
        currentnuminchain = nextnuminchain
    if chainlength >= maxchainlength[1]:
        maxchainlength = [i, chainlength]

print(maxchainlength)










