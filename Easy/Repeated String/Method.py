#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """ At first i was thinking like some where i would repeat the string n times then call the count function. It's logically true but practically for a pc its an out of memory error. So the idea is to count the "a" in the original string and multiply with number of times that will satisfy the string length of the required multiplication times (n//len(s)) but there is also a problem when the length is not evenly divided by n so we need to add the partial length and count the "a"s in it ( s[:(n%len(s))].count("a") )"""
    return (s.count("a") * (n//len(s)) + s[:n % len(s)].count("a"))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

