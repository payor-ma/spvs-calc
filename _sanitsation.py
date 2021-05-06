#!/usr/bin/env python3

import sys
from _constants import *

def checkSexDigit(sexStrDigit):
    try:
        if sexStrDigit == "" or sexStrDigit == " ":
            sexStrDigit = "0"

        sexDigit = int(sexStrDigit)
        if sexDigit > 59:
            raise ValueError("Digit above 59.")
        if sexDigit < 0:
            raise ValueError("Digit negative.")
        return sexDigit
    except ValueError:
        sys.exit("Invalid sexagesmial number inputted")