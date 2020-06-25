#!/bin/python3
from math import pow

a, b, c = input(), input(), input()
print("{}\n{}".format(int(pow(a,b)), ((a**b)%c)))
