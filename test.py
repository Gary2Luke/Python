#!/usr/bin/python
# coding = UFT-8

import os

clear = file('chuli.txt','wb')
name = 'firefox'
m='whereis %s >>chuli.txt' %name
os.system(m)
lines = file('chuli.txt','r')
for line in lines:

    line = line.replace('\n','')
    line = line.split(' ')
    for i in range(1,len(line)):
        print line[i]