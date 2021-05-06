#!/usr/bin/env python3

from conversions import *

#robust to multiple zero formats, see help statement
#prints out using zero to be unambiguous
# * doesnt work cause command line

#functions to support
# multiply
# add
# subtract
# invert / divide ??
# factorise

PATT_HELP = ("-h", "h", "-H", "H", "HELP", "help", "Help", "-help", "--help")
PATT_MULT = ("mult", "Mult", "multiply", "Multiply", "m", "M", "-m", "-M")
PATT_ADD =  ("+", "add", "Add", "plus", "Plus", "a", "A", "-a", "-A")
PATT_SUB = ("-", "sub", "Sub", "subtract", "Subtract", "s", "S", "-s", "-S")

HELP_GENERAL = "SPVS (sexagesimal) calculator script.  Currently supports multiply, add, subtract.\nUsage:\n\tadd <a> <b>\n\tsub <a> <b>\n\tmult <a> <b>\nInfix is also supported with \'+\', \'-\' and \'x\'.\nNote that for infix multiplication, the letter \'x\' must be used, as \'*\' is a special character.\nUse argument \'h\' or \'help\' for extended usage options."
HELP_MULT = "Mul"
HELP_ADD = "Help for add"
HELP_SUB = "Help for subtract"
HELP_EXTENDED = HELP_GENERAL[:-55] + "\n\nAccepted commands for prefix are as follows.\nMultiply:\t" + ",".join(PATT_MULT) + "\nAdd:\t\t" + ",".join(PATT_ADD) + "\nSubtract:\t" + ",".join(PATT_SUB) + "\nAccepted infix symbols are \'+\' for add, \'-\' for subtract and \'x\' (as in the letter) for multiply."

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