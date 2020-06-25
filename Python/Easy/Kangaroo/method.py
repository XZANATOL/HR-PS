#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #if second kangaroo has a distance and velocity bigger than the first
    if x2>x1 and v2>v1:
        return("NO")
    #if not
    else:
        #check if the kangaroos will meet (10000 value is put according to the test limit of the problem)
        for i in range(0,10000):
            x1+=v1
            x2+=v2
            if x1==x2:
                #if triggered, it will break the loop
                return("YES")
        #in case of "if statement" is not triggered in the for loop
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

