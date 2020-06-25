#!/bin/python3
#This method is built on only sorting the array

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #Sorting array
    ar.sort()

    #Assigning variables
    a = ar[len(ar)-1]
    i = len(ar) -1
    count = 0

    #Check loop
    while i > -1:
        if ar[i] == a:
            count +=1
            i = i - 1
        else:
            break
    
    #Returning count
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

