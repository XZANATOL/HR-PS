#!/bin/python3
def print_rangoli(size):
    #make a list of alphabets depending on size value
    alphabet = ["abcdefghijklmnopqrstuvwxyz"[i] for i in range(n)]
    #make a list of indexes depending on size value
    l = list(range(size))
    l = l[:-1] + l[::-1]
    #print loop
    for i in l:
        prin = alphabet[-(i+1):]
        """
                                    break down
            "-".join to join the following list of
            prin[::-1] (which is a reversed list) + prin[1:] (which is to slice the first element as to not be repeated)
            then comes the alignment part of .center()
            the size*4-3 is the width of any rangoli
            and the "-" is for filling spaces between the join
        """
        print("-".join(prin[::-1] + prin[1:]).center(size*4-3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
