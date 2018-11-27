#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     29/03/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
from collections import Counter
import time

start = time.time()

p = []

for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt((a**2)+(b**2))
        if c % 1 == 0:
            tot = a+b+c
            if tot <= 1000:
                p.append(tot)

count = Counter(p)

print(count.most_common(1))

end = time.time()

runtime = end - start
print(runtime)











