#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

lib_sum = []
path = '/home/sonny/Analyze_library'
summarize = file('summarize.txt','w')

# usrbinlibrary = file('/home/sonny/usrbin_library.txt')
# for line2 in usrbinlibrary.readlines():
#     line2 = line2.split(',')
#     if line2[0] not in lib_sum:
#         lib_sum.append(line2[0])

for f in os.listdir(path):
    if 'library.txt' in f:
        g = open(path+'/'+f)

        for line in g.readlines()[0:20]:
            line=line.split(',')
            # line = line.replace(',',':')
            if line[0] not in lib_sum:
                lib_sum.append(line[0])

#
for item in lib_sum:
    print item.split('/')[-1].replace('\'','')
