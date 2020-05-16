#!/bin/python3

import math
import os
import random
import re
import sys
#imporing reduce function.. my savior..
from functools import reduce
#import gcd function cuz im lazy to fetch gcd formula
from math import gcd as gcda

def getTotalX(a, b):
    #Computing gcd
    def gcd(a, b):
        return gcda(a,b)
    #Computing lcm 
    def lcm(a, b):
        return a * b // gcd(a, b)
 
    #reduce
    finalgcd, finallcm = reduce(gcd, b), reduce(lcm, a)
    #obtaining the list length of b list factors
    result = sum([1 for i in range(finallcm, finalgcd+1, finallcm) if finalgcd % i == 0])
    #printing the result
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
