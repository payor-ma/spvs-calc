#!/usr/bin/env python3

from _strings import *
from _functions import *

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


#    print(twoDigitInverse("20"))

# forgive me but I don't like argparse so we're doing this with an IF    block
def main(argv):
    cullFlag = False
    result = "No output."

    if len(argv) == 0:
        help(HELP_GENERAL)

    #option parsing
    if argv[0] in PATT_CULL:
        argv = argv[1:]
        cullFlag = True


    #command parsing
    if argv[0] in PATT_HELP:
        help(HELP_EXTENDED)
    if argv[0] in PATT_MULT:
        result = help(HELP_MULT) if len(argv) < 3 else multSex(argv[1],argv[2])
    elif argv[0] in PATT_ADD:
        result = help(HELP_ADD) if len(argv) < 3 else addSex(argv[1],argv[2])
    elif argv[0] in PATT_SUB:
        result = help(HELP_SUB) if len(argv) < 3 else subSex(argv[1],argv[2])
    elif argv[0] in PATT_INV:
        if len(argv) < 2:
            help(HELP_INV)
        elif len(argv) < 3:
            result = bruteInverse(argv[1],-1)
        else:
            result = bruteInverse(argv[1],int(argv[2]))

    #others here
    

    #infix support!
    elif argv[1] == "x":
        result = multSex(argv[0],argv[2])
    elif argv[1] == "+":
        result = addSex(argv[0],argv[2])
    elif argv[1] == "-":
        result = subSex(argv[0],argv[2])
    else:
        help(HELP_GENERAL)

    if result == None:
        print("No result found.")
    else:
        output = stripZeroes(result) if cullFlag else result
        print(output)

    sys.exit(0)



if __name__ == "__main__":
   main(sys.argv[1:])