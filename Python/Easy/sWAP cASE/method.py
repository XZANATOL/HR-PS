#!/bin/python3
#check the letter status function
def check(letter):
    if letter.isupper():
        letter = letter.lower()
    elif letter.islower():
        letter = letter.upper()
    else:
        return letter
    return letter

def swap_case(s):
    #A variable to save the switched string
    string = ""
    for i in s:
        #check the letter status and add it to the variable
        string += check(i)
    #return the switched statement
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
