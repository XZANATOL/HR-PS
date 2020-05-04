#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    #assigning variables
    length = len(str(n))
    i = 0
    count = 0
    while i <= length-1:
        #to avoid divide by zero error
        if int(str(n)[i]) == 0:
            i+=1
            continue
        #try the division reminder
        elif n%int(str(n)[i]) == 0:
            count += 1
        i+=1
    #return value
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

