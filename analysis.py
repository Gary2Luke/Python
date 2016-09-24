#!/usr/bin/python
# coding = UFT-8
from collections import Counter
result = []
b={}
fd = file("/home/sonny/2.txt", "r")

for line in fd.readlines():
    line = line.strip('\n')
    line = line.strip('\t')

    result.append(line)
# myset = set(result)
# print(myset)
b=Counter(result)
print b
# for x in b.items():
#     print x

