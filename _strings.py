#!/usr/bin/env python3

PATT_HELP = ("-h", "h", "-H", "H", "HELP", "help", "Help", "-help", "--help")
PATT_MULT = ("mult", "Mult", "multiply", "Multiply", "m", "M", "-m", "-M")
PATT_ADD =  ("+", "add", "Add", "plus", "Plus", "a", "A", "-a", "-A")
PATT_SUB = ("-", "sub", "Sub", "subtract", "Subtract", "s", "S", "-s", "-S")

HELP_EX = "e.g. \'12.34.56\'."
HELP_NUM = "Where <a> and <b> are SPVS numbers,"+ HELP_EX
HELP_ZERO = "Accepts zeros of the form \'1.0.2\', \'1..2\', and \'1. .2\'."
HELP_GENERAL = "SPVS (sexagesimal) calculator script.\nSPVS Digits deliminated by periods (\'.\'), "+HELP_EX+"\n"+HELP_ZERO+"\n\nCurrently supports multiply, add, subtract.\nUsage:\n\tadd <a> <b>\n\tsub <a> <b>\n\tmult <a> <b>\nInfix is also supported with \'+\', \'-\' and \'x\'.\nNote that for infix multiplication, the letter \'x\' must be used, as \'*\' is a special character.\nUse argument \'h\' or \'help\' for extended usage options."
HELP_MULT = "Usage:\n\tmult <a> <b> OR <a> x <b>\n" + HELP_NUM + "\n" + HELP_ZERO
HELP_ADD = "Help for add"
HELP_SUB = "Help for subtract"
HELP_EXTENDED = HELP_GENERAL[:-55] + "\n\nAccepted commands for prefix are as follows.\nMultiply:\t" + ",".join(PATT_MULT) + "\nAdd:\t\t" + ",".join(PATT_ADD) + "\nSubtract:\t" + ",".join(PATT_SUB) + "\n\nAccepted infix symbols are \'+\' for add, \'-\' for subtract and \'x\' (as in the letter) for multiply."
