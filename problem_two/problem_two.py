#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    test = False
    while (test == False):
        s = input("Qual a hora a ser convertida?")
        if not s.upper().endswith('AM') and not s.upper().endswith('PM'):
            print("Valor de entrada inválido. Formato esperado: HH:MM:SSTT (TT = AM ou PM)")
        else:
            test = True
    period = s[-2:]
    time = s[:-2]
    hh, mm, ss = time.split(':')
    hh = int(hh)
    if period == "AM":
        # Caso especial para 12 AM
        if hh == 12:
            hh = 0
    else:  # PM
        # Caso especial para 12 PM
        if hh != 12:
            hh += 12
    hh = f"{hh:02}"
    return f"{hh}:{mm}:{ss}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
