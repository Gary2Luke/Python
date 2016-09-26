#!/usr/bin/python
# coding = UFT-8
import re
from collections import Counter

result = []
b={}
fd = file("/home/sonny/2.txt", "r")


for line in fd.readlines():

    line = line.strip()

    # print re.findall("(?<=()+\.[^()]+(?=[)])", line)
    print re.findall("(?<=[(])+(?=[)])", line)

    result.append(line)
# myset = set(result)
# print(myset)
b=Counter(result)
print b
# # d = sorted(s.iteritems(), key=lambda t: t[1], reverse=False)
# for x in b.items():
#     print x
