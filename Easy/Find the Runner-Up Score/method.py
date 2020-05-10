#!/usr/bin/python3
if __name__ == '__main__':
    n = int(input())
    #to make a str list
    arr = input().split(" ")
    #converting str elements to int
    arr = [int(i) for i in arr]
    #reverse sorting for faster results
    arr.sort(reverse=True)
    #getting the runner-up score value
    for i in arr:
        if i < arr[0]:
            #printing result
            print(i)
            #exit on triggering
            break
