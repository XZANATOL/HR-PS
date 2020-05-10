#!/usr/bin/python3
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n])
    
    """
    Using list compression in python3 to try every possiblity whose sum of the 3-dimensions doesn't equal n

    for X in range(0,y+1)
    we use the "+1" to implement the y value inside the range
    """
