#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges, m, n):
    #define house x-axis range
    housecoord = range(s,t+1)
    #count variables
    countapples = 0
    countoranges = 0

    #detecting the fall distance of each fruit
    for i in range(0, m):
        apples[i] += a
    for i in range(0, n):
        oranges[i] += b

    #check if values intersect with house coordinates and increment count by 1
    for i in apples:
        if i in housecoord:
            countapples +=1
    for i in oranges:
        if i in housecoord:
            countoranges +=1
    
    #print values
    print(str(countapples) + "\n" + str(countoranges))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges, m, n)

