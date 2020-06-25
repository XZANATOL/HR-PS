#!/bin/python3
# Like i did manage to convert it to indicies but in the end the secret of the challenge was to use the fkin enumerate function in list (q) to return both index and value instead of fetching the index by itself...

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves=0
    # Converting list numbers into indicies
    q = [value-1 for value in q]


    for index,value in enumerate(q):
        # If moved more than 2
        if (value - index) > 2:
            print("Too chaotic")
            return 0

        #check moved distance and add it to moves variable
        for k in range(max(value-1,0), index):
            if q[k] > value:
                moves+=1
    print(moves)
        
    



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

