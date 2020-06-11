#!/bin/python3
#My first regular expression code (can hardly understand it tho xd)
import re

pattern = re.compile(
    #make sure that all characters are either numeric or hyphen "-" using the inverse search ?!
    r'(?!.*(\d)(-?\1){3})'
    #make sure that the string begins with 4,5, or 6 with the search of numbers of length 3
    r'^[4-6]\d{3}'
    #this to avoid the presence of unorganised hyphen orders 12345678-1234. In addition to, make sure to digits are repeated more than 4 times
    r'(\d{12}|(-?\d{4}){3})'
    r'$'
    )

for i in range(int(input())):
    if pattern.search(input()):
        print("Valid")
    else:
        print("Invalid")

