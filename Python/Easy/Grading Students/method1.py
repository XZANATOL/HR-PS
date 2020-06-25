#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    #Assigning local variables
    final=""
    #check loop
    for i in grades:
        temp = i
        #while loop for making temp variable equals to the next multiple of 5
        while temp%5 !=0:
            temp+=1
        #check degree conditions
        if temp-i <3 and temp > 39:
            final += str(temp)+"\n"
        else:
            final += str(i)+"\n"
    #returning result
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write(''.join(map(str, str(result))))
    fptr.write('')

    fptr.close()

