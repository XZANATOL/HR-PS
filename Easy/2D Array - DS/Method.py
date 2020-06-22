#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # Greatest value keeper
    count = -1000

    # Hourglass Counters initial values
    cutter = 0
    middle_element = 1

    # Hourglass initial Level values
    upper_row = 0
    middle_row = 1
    lower_row = 2

    # Beginning of the game :)
    while lower_row < 6:

        # Hourglass summator loop
        while middle_element != 5:
            temp = arr[upper_row][cutter] + arr[upper_row][cutter+1] + arr[upper_row][cutter+2] + arr[middle_row][middle_element] + arr[lower_row][cutter] + arr[lower_row][cutter+1] + arr[lower_row][cutter+2]
            #Compare if the value is bigger than the current value (if yes then replace)
            if temp > count:
                count = temp

            # Increament counters by 1
            cutter+=1
            middle_element +=1
        
        # Navigate Hourglass summator 1 level down and reset counters values
        upper_row+=1
        lower_row+=1
        middle_row+=1
        cutter=0
        middle_element=1

    # After the loop Finished return the greatest value calculated
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

