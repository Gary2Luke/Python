#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(1,221):
    i = str(j).rjust(3, '0')
    k='/home/sonny/code/%s/%d' %(i,j)

    if os.path.exists(k):


        m='rm /home/sonny/code/%s/%d' %(i,j)


        os.system(m)






