#!/bin/python3
"""
This depends on slicing.. well, more faster tho and a one line solution
"""
import math
import os
import random
import re
import sys

def rotLeft(arr, length, rotations):
    return arr[rotations:] + arr[:rotations]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    # Rotation Loop
    result = rotLeft(a, n, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

