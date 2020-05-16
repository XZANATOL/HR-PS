#!/bin/python3
def mutate_string(string, position, character):
    string = list(string)
    string[position] = str(character)
    string = "".join(string)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
