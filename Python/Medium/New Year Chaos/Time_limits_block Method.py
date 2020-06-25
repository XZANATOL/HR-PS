#!/bin/python3
# Unfortunately this method is correct but did not finish in the time limits for test cases 6-9 :\
# So what i was doing is making a reference list then check with it's indecies, I think this challenge wants me to deal only with one list so what i will do in the correct one is to convert the original list's numbers into indecies using (value-1) function

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves=0
    # A reference list to check from
    checker = sorted(q)
    for i in range(0,len(q)):
        if q[i] - checker[i] > 2:
            print("Too chaotic")
            # Well, a foolish move to use sys.exit() as this will exist the testing script xD
            return 0

        re = checker.index(q[i])
        for k in range(max(re-1,0), i):
            if q[k] > re:
                moves+=1
    print(moves)
        
    



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

