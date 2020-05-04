#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    #assigning variables
    i = n
    result = 1
    #factorial loop
    while i != 0:
        result = result * i
        i -=1
    #printing result
    print(result)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)



