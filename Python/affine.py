#-------------------------------------------------------------------------------
# Name:        Affine
# Purpose:     Encoding and decoding affine ciphers
#
# Author:      Richard Li
#
# Created:     14/02/2020
# Copyright:   (c) Richard Li 2020
# Licence:     MIT
#-------------------------------------------------------------------------------
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
encoded = []
check = 0
finalencode = []
finaldecode = []

ainput = input("a")
a = int(ainput)
binput = input("b")
b = int(binput)
message = input("message")
messagelist = list(message.lower())

for i in numbers:
    encoded.append(((a*i)+b)%26)

for c in messagelist:
    hi = letters.index(c)
    hi1 = encoded[hi]
    finalencode.append(letters[hi1])

for d in messagelist:
    ha = letters.index(d)
    ha1 = encoded.index(ha)
    finaldecode.append(letters[ha1])

outputencode = ''.join(finalencode)
outputdecode = ''.join(finaldecode)

print(outputencode)
print(outputdecode)



