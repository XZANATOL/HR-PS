#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    #initial variable
    initial = 0
    for i in arr:
        #check which number is repeated more to declare the number of deletions
        if arr.count(i)>initial:
            initial = arr.count(i)
    #to get a list of all similar numbers and max repeatetions, the minimal deletion value must be set to delete the other different values>> in mathematical form (similars = list_length - odd_numbers(deletions) >> deletions = list_length-similars)
    return len(arr)-initial


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

