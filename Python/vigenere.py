#-------------------------------------------------------------------------------
# Name:        Vigenere
# Purpose:     Encoding and decoding vigenere ciphers
#
# Author:      Richard Li
#
# Created:     14/02/2020
# Copyright:   (c) Richard Li 2020
# Licence:     MIT
#-------------------------------------------------------------------------------
import time

print("Program to encode and decode vigenere ciphers")
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

keywordstring = input("Enter the keyword: ")
messagestring = input("Enter the message to be encoded or decoded, without spaces: ")

firstkeywordlist = list(keywordstring.lower())

keywordlist = []
messagelist = list(messagestring.lower())
encodelist = []
decodelist = []

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

inletter = 0
for letter in messagelist:
    keywordlist.append(firstkeywordlist[inletter % len(firstkeywordlist)])
    inletter += 1

var1 = 0
for creativename in messagelist:
    var2 = keywordlist[var1]
    var3 = alphabet.index(creativename)
    var4 = alphabet.index(var2)
    encoded = alphabet[(var3 + var4) % 26]
    encodelist.append(encoded)
    var1 += 1

coolvar1 = 0
for anothername in messagelist:
    coolvar2 = keywordlist[coolvar1]
    coolvar3 = alphabet.index(anothername)
    coolvar4 = alphabet.index(coolvar2)
    decoded = alphabet[(26 + coolvar3 - coolvar4) % 26]
    decodelist.append(decoded)
    coolvar1 += 1

outputencode = ''.join(encodelist)
outputdecode = ''.join(decodelist)

print("")
print("")
print("Encoded message: ",outputencode)
print("Decoded message: ",outputdecode)
print("")
print("")

waittime = input("Press Enter to exit.")






