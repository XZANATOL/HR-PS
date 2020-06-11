#!/bin/python3
#That's a solution of an Engineer not a lazy programmer xd
from math import sqrt, acos, degrees
#Get sides of triangle
AB = int(input())
BC = int(input())
#Get Hypotinouse length
AC = sqrt((AB**2)+(BC**2))
#Get median length using Euclidean theorem
BM = (AB*BC)/AC
#using math.acos (cos-1()) to return the angle in radian and converts it into degrees using math.degrees
angle = round(degrees(acos(BM/BC)))

#To check acute angles
if BM<BC:
    angle-=90
    #To check if negative
    if angle<0:
        angle*=-1

#The inserted 1 to approximate it to the nearest 1 decimal place
angle = round(angle,1)

#The following is because of the round() function error when it comes to 0.5 approximation

#Check if the decimal place is 5
if str(angle)[-1] == "5":
    #Then round it as 0.6 not 0.5
    angle = round(angle+0.1)
else:
    #Else just round it whatever the value as it will be correct
    angle = round(angle)

#Print the Result
print(str(int(angle))+"°")
