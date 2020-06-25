#!/bin/python3
import textwrap

def wrap(string, max_width):
    # count variable to add a newline for the max_width value
    count = 0
    # string after wrapping variable
    output = ""
    # convert into list
    string = list(string)
    # wrapping loop
    for i in string:
        output += i
        count +=1
        if count % max_width == 0:
            output += "\n"
    #retrun wrapped string
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
