#!/bin/python3
import sys

#Just lazy to remember the map function xd
l = input().split()
N = int(l[0])
M = int(l[1])

#Check mat size
if not M/N == 3:
    print("Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)")
    sys.exit(1)

#Loop for the upper part
for i in range(1,int((N-1)), 2):
    print((".|."*i).center(M, "-"))

#Welcome statement
print("WELCOME".center(M, "-"))

#Same loop but for the lower part
for i in range(1,int((N-1)), 2)[::-1]:
    print((".|."*i).center(M, "-"))
