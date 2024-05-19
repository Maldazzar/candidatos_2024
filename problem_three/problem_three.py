#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    print("Digite a quantidade de números que deseja ordenar (entre 1 e 1 milhão):")
    n = int(input().strip())
    if n < 1 or n > 1000000:
        print("O número deve estar entre 1 e 1 milhão.")
    else:
        numbers = []
    print(f"Digite {n} números inteiros:")
    for _ in range(n):
        number = int(input().strip())
        numbers.append(number)
    numbers.sort()
    print("Números ordenados:")
    for number in numbers:
        print(number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
