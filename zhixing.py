#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(1,210):
    i = str(j).rjust(3, '0')
    k='/home/sonny/code/%s/%d_static' %(i,j)
    if os.path.exists(k):

        print '************%d*************' %j
        os.system(m)
        print '\n'






