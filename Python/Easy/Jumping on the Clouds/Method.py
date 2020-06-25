#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #initial variables
    jumps=0
    i=0
    while i < len(c):
        #for every jump (doesn't matter the distance yet)
        jumps+=1
        #if the second index = 0, increase i by 1 (so it's increased by 2) (i<len(c)-2 to avoid out of index error)
        if i < len(c)-2 and c[i+2] ==0:
            i+=1
        i+=1
    #the loop will get launched again when i is equal to the last index of the list
    return jumps-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

