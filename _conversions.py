#!/usr/bin/env python3

from _sanitsation import *

# converts a sexagesimal string into an integer
def toDec(sexStr):
    return sexListToDec(sexToSexList(sexStr))

# converts an integer (what the computer is using to do the math) to a sexagesimal string
def toSex(decNum):
    return sexListToSex(decToSexList(decNum))


# smaller functions to enable the above functions
def sexToSexList(sexStr):
    return [checkSexDigit(i) for i in sexStr.split(".")] # runs thru sanitisation on input checking

def sexListToDec(sexList):
    numDigits = len(sexList)
    accumulator = 0
    for i in range(numDigits):
        accumulator += sexList[i]*(BASE**(numDigits-i-1))
    return accumulator

def decToSexList(decNum):
    if decNum == 0:
        return [0]
    sexDigits = []
    while decNum:
        sexDigits.append(int(decNum % BASE))
        decNum //= BASE
    return sexDigits[::-1]

def sexListToSex(sexList):
    return ".".join([str(i) for i in sexList]

)

# not designed to take unsanitised, only for stuff that's gone thru check before
def stripZeroes(sexStr):
    sexList = sexStr.split(".")
    for i in range(len(sexList)-1,0,-1):
        if sexList[i] == "0":
            sexList.pop(i) 
        else:
            break
    return sexListToSex(sexList)