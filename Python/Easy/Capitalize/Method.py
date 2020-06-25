#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    count = 0
    #split names
    s = list(s)
    #output variable
    output = ""
    #loop of conversion
    s[0] = s[0].upper()
    while count < len(s):
        #check for spaces (to determine words beginnings)
        if s[count] == " ":
            s[count+1] = s[count+1].upper()
        #add each char (even after capitalization) to output variable
        output += s[count]
        #increase count to loop through each char
        count+=1
    #return output
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

