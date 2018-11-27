#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     31/01/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

start = time.time()

working = 1
working1 = 1
final = 1

for hi in range(1, 25):
    for i in range(1, 30):
        print(final)
        final = working + working1
        working = working1
        working1 = final

end = time.time()
tottime = end-start
avtime = tottime/250
print(avtime)