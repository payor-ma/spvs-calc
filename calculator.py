#!/usr/bin/env python3

from _conversions import *
from _strings import *

#robust to multiple zero formats, see help statement
#prints out using zero to be unambiguous
# * doesnt work cause command line

#functions to support
# multiply
# add
# subtract
# invert / divide ??
# factorise

def help(printString):
    print(printString)
    sys.exit(0)

def multSex(sexA,sexB):
    print (toSex(toDec(sexA)*toDec(sexB)))

def addSex(sexA,sexB):
    print (toSex(toDec(sexA)+toDec(sexB)))

def subSex(sexA,sexB):
    result = toDec(sexA)-toDec(sexB)
    if result < 0:
        print("Result was negative.  Absolute value provided.")
    print (toSex(abs(result)))

# forgive me but I don't like argparse so we're doing this with an IF    block
def main(argv):
    if len(argv) == 0:
        help(HELP_GENERAL)

    #command parsing
    if argv[0] in PATT_HELP:
        help(HELP_EXTENDED)
    if argv[0] in PATT_MULT:
        help(HELP_MULT) if len(argv) < 3 else multSex(argv[1],argv[2])
    elif argv[0] in PATT_ADD:
        help(HELP_ADD) if len(argv) < 3 else addSex(argv[1],argv[2])
    elif argv[0] in PATT_SUB:
        help(HELP_SUB) if len(argv) < 3 else subSex(argv[1],argv[2])

    #others here
    

    #infix support!
    elif argv[1] == "x":
        multSex(argv[0],argv[2])
    elif argv[1] == "+":
        addSex(argv[0],argv[2])
    elif argv[1] == "-":
        subSex(argv[0],argv[2])
    else:
        help(HELP_GENERAL)

    sys.exit(0)



if __name__ == "__main__":
   main(sys.argv[1:])