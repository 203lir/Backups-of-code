#-------------------------------------------------------------------------------
# Name:        Matrix
# Purpose:     Encoding and decoding matrix ciphers
#
# Author:      Richard Li
#
# Created:     11/3/2020
# Copyright:   (c) Richard Li 2020
# Licence:     MIT
#-------------------------------------------------------------------------------
import time
import numpy

print("Program to encode and decode matrix ciphers")
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
print("|a b|")
print("|c d|")
print("")
print("")
ainput = input("Enter the value of a: ")
reala = int(ainput)
binput = input("Enter the value of b: ")
realb = int(binput)
cinput = input("Enter the value of c: ")
realc = int(cinput)
dinput = input("Enter the value of d: ")
reald = int(dinput)
keymatrix = [[reala, realb], [realc, reald]]
orig1 = input("Enter the message to be encoded or decoded, without spaces: ")
orig = orig1.lower()
print("")
print("")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def transform(var1):
    transformlist = list(var1)
    list1 = []
    list2 = []
    var2 = 0
    for a in transformlist:
        if var2 % 2 == 0:
            list1.append(a)
        else:
            list2.append(a)
        var2 += 1
    output = []
    output.append(list1)
    output.append(list2)
    return output

def untransform(stupid):
    outputlist = []
    for i in range(len(stupid[0])):
        outputlist.append(stupid[0][i])
        outputlist.append(stupid[1][i])
    output = ''.join(outputlist)
    return output

def modinverse(i):
    for a in range(26):
        if (i*a)%26 == 1:
            return a

def letterencode(inmatrix):
    outmatrix = []
    for a in inmatrix:
        workinglist = []
        for b in a:
            workinglist.append(alphabet.index(b))
        outmatrix.append(workinglist)
    return outmatrix

def letterdecode(inmatrix):
    outmatrix = []
    for a in inmatrix:
        workinglist = []
        for b in a:
            workinglist.append(alphabet[b])
        outmatrix.append(workinglist)
    return outmatrix

def matrixmultiply(key, message):
    result = numpy.dot(key, message)
    return result

def decipherkey(key):
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    determinant = a*d-b*c
    newa = d
    newb = (-1*b)+26
    newc = (-1*c)+26
    newd = a
    determinantrecip = modinverse(determinant)
    finala = (newa*determinantrecip)%26
    finalb = (newb*determinantrecip)%26
    finalc = (newc*determinantrecip)%26
    finald = (newd*determinantrecip)%26
    output = [[finala, finalb], [finalc, finald]]
    return output

def simplifymatrix(matrix):
    output = []
    for a in matrix:
        workingoutput = []
        for b in a:
            workingoutput.append(b%26)
        output.append(workingoutput)
    return output


numbermessage = letterencode(transform(orig))
encodednumber = simplifymatrix(matrixmultiply(keymatrix, numbermessage))
finalencoded = untransform(letterdecode(encodednumber))
print("Encoded message: ", finalencoded)

decodekey = decipherkey(keymatrix)
decodednumber = simplifymatrix(matrixmultiply(decodekey, numbermessage))
finaldecoded = untransform(letterdecode(decodednumber))
print("Decoded message: ", finaldecoded)

print("")
print("")
waittime = input("Press Enter to exit.")
print(waittime)





