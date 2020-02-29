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
import time

print("Program to encode and decode affine ciphers")
print("")
print("")
print("MIT License")
print("")
print("Copyright © 2020 Richard Li")
print("")
print("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:")
print("")
print("The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.")
print("")
print("THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
print("")
print("")

time.sleep(2)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
encoded = []
check = 0
finalencode = []
finaldecode = []

ainput = input("Enter the value of a: ")
a = int(ainput)
binput = input("Enter the value of b: ")
b = int(binput)
message = input("Enter the message to be encoded or decoded: ")
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

print("")
print("")
print("Encoded message: ",outputencode)
print("Decoded message: ",outputdecode)
print("")
print("")

waittime = input("Press Enter to exit.")

