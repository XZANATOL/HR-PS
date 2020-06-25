#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #assigning variables
    A=0
    i=0
    count=0
    #counting valley loop
    while i<n:
        #Determine his position respecting to sea level
        if s[i]=="U":
            A = A+1
        elif s[i]=="D":
            A= A-1
        #triggers when leaving a valley
        if s[i]=="U" and A==0:
            count+=1
        #checking the next term index
        i+=1
    #returning the result
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

