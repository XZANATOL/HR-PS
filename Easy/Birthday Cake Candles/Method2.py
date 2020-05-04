#!/bin/python3
#This method is built on sorting and reversing the array

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    #Sorting array
    ar.sort()
    ar.reverse()

    #Assigning variables
    a = ar[0]
    i = 0
    count = 0

    #Check loop
    while i < len(ar):
        if ar[i] == a:
            count +=1
            i = i + 1
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

