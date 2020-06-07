#!/bin/python3
def print_formatted(number):
    #count variable, alignment variable
    i = 1
    w = len(bin(number)[2:])

    #print loop
    while i <= number:
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[2:]).upper().rjust(w, ' '), str(bin(i)[2:]).rjust(w, ' '))
        i+=1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
