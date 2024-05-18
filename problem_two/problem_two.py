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
    s = s[-9:-3]
    hora, minuto, segundo = s.split(':')
    if s.upper().endswith('PM'):
        hora = int(hora) + 12
    hora_str = hora
    minuto_str = f'{minuto:02}'
    segundo_str = f'{segundo:02}'
    military = f'{hora_str}:{minuto_str}:{segundo_str}'
    print(military)       
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
