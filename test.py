#!/usr/bin/python
# coding = UFT-8

import os

f=file('/home/sonny/usrbindynamic.txt','r')

info=f.readlines()
for line in info:
    k=line.split(',')[0].replace('\'','')
    # print k
    m='cp %s /home/sonny/benchmark/library' %k
    # print m
    os.system(m)