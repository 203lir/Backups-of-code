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
import math
def catalan_numbers(n):
    n1 = 2*n
    n2 = 1+n
    n3 = math.factorial(n1)
    n4 = math.factorial(n)
    n5 = math.factorial(n2)
    final1 = n4*n5
    final2 = n3/final1
    return int(final2)

input = input("Enter the catalan number index")
process = int(input)
print(catalan_numbers(process))