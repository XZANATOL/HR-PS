#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    #Sorting array
    arr.sort()

    #Defining summation variables
    i = 0
    mini = 0
    maxi = 0
    
    #Minimum summation loop
    while i <= 3:
        mini += arr[i]
        i+=1
    
    #Reseting i
    i = 1
    
    #Maximum summation loop
    while i <= 4:
        maxi += arr[i]
        i+=1
    
    #Printing Results
    print(str(mini) + " " + str(maxi))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
