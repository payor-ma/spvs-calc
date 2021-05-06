#!/usr/bin/env python3

PATT_HELP = ("-h", "h", "-H", "H", "HELP", "help", "Help", "-help", "--help")
PATT_MULT = ("mult", "Mult", "multiply", "Multiply", "m", "M")
PATT_ADD =  ("add", "Add", "plus", "Plus", "a", "A")
PATT_SUB = ("sub", "Sub", "subtract", "Subtract", "s", "S")
PATT_INV = ("inv", "Inv", "i", "I", "invert", "Invert", "Inverse", "inverse")
PATT_CULL = ("-c", "--c", "--cull", "-C")

HELP_EX = "e.g. \'12.34.56\'."
HELP_NUM = "Where <a> and <b> are SPVS numbers,"+ HELP_EX
HELP_ZERO = "Accepts zeros of the form \'1.0.2\', \'1..2\', and \'1. .2\'."
HELP_GENERAL = "SPVS (sexagesimal) calculator script.\nSPVS Digits deliminated by periods (\'.\'), "+HELP_EX+"\n"+HELP_ZERO+"\n\nCurrently supports multiply, add, subtract and a bruteish inverse search. \nUsage:\n\tadd <a> <b>\n\tsub <a> <b>\n\tmult <a> <b>\n\tinv <a> <digitDepth>\nInfix is also supported with \'+\', \'-\' and \'x\'.\nNote that for infix multiplication, the letter \'x\' must be used, as \'*\' is a special character.\nUse argument \'h\' or \'help\' for extended usage options."
HELP_MULT = "Usage:\n\tmult <a> <b> OR <a> x <b>\n" + HELP_NUM + "\n" + HELP_ZERO
HELP_ADD = "Usage:\n\tadd <a> <b> OR <a> + <b>\n" + HELP_NUM + "\n" + HELP_ZERO
HELP_SUB = "Usage:\n\tsub <a> <b> OR <a> - <b>\n" + HELP_NUM + "\n" + HELP_ZERO + "\nIf the result of a subtraction is negative, the result will be the absolute value."
HELP_INV = "Usage:\n\tinv <a> <digitDepth>\n" +  "Where <a> is an SPVS number, and <digitDepth> is the max amount of digits to search for an inverse.\n" + HELP_ZERO + "\nThis function is completely unoptimised and bruteish.\nAs such the maximum number of digits for <digitDepth> is capped at 3 and defaults to 2."
HELP_EXTENDED = HELP_GENERAL[:-55] + "\n\nAccepted commands for prefix are as follows.\nMultiply:\t" + ",".join(PATT_MULT) + "\nAdd:\t\t" + ",".join(PATT_ADD) + "\nSubtract:\t" + ",".join(PATT_SUB) + "\nInvert:\t" + ",".join(PATT_INV) + "\n\nAccepted infix symbols are \'+\' for add, \'-\' for subtract and \'x\' (as in the letter) for multiply."
