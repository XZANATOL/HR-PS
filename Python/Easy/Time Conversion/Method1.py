#!/bin/python3
#There is an error in f.write(str(result) + '\n') -> str() should be added to result 

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    output = ""
    temp = 0
    slicerAM = slice(0,8)
    slicerPM1 = slice(0,2)
    slicerPM2 = slice(2,8)
    if "12" in str(s) and "AM" in str(s):
        output = "00" + s[slicerPM2]
    elif "AM" in str(s):
        output = s[slicerAM]
    elif "12" in str(s) and "PM" in str(s):
        output = s[slicerAM]
    elif "PM" in str(s):
        temp = int(s[slicerPM1]) + 12
        output = str(temp) + s[slicerPM2]
    return output

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(str(result) + '\n')

    f.close()
