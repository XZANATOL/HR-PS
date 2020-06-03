#!/bin/python3
"""
The code is correct but it depends on array cycling so won't exceute in the limited times (as in test case 8 and 9)
"""
import math
import os
import random
import re
import sys

def rotLeft(arr, length, rotations):
    # save first element as it will be first to be over written
    for i in range(0,rotations):
        temp = arr[0]
        # Rotation loop
        for i in range(0,length-1):
            arr[i] = arr[i+1]
        # put first original first element
        arr[i+1] = temp
    # Return rotated array
    return arr

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

