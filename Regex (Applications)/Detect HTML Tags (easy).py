#!/usr/bin/python3
import re

selfclose_pattern = r'</?(\w+)( ?)'
list = []

for i in range(int(input())):
    result = re.findall(selfclose_pattern, input())
    for i in result:
        for l in i:
            if len(l) > 0 and l not in list and l != " ":
                list.append(l)

print(';'.join(sorted(list)))
