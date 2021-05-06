#!/usr/bin/env python3

from _conversions import *

def multSex(sexA,sexB):
    return (toSex(toDec(sexA)*toDec(sexB)))

def addSex(sexA,sexB):
    return (toSex(toDec(sexA)+toDec(sexB)))

def subSex(sexA,sexB):
    result = toDec(sexA)-toDec(sexB)
    if result < 0:
        print("Result was negative.  Absolute value provided.")
    return (toSex(abs(result)))

def bruteInverse(sex,digitDepth):
    if digitDepth < 1 or digitDepth > 3:
        print("Specified <digitDepth> out of the accepted range [1,3].  Defaulting to 2.")
        digitDepth = 2
    for i in range(2,BASE**digitDepth):
        if stripZeroes(toSex(toDec(sex)*i)) == "1":
            return toSex(i)
    return None
    