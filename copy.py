#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(1,221):
    i=str(j).rjust(3, '0')
    k='/home/sonny/sourcecode/%d.c' %j
    h='/home/sonny/code/%s' %i
    if os.path.exists(k):


        m='cp /home/sonny/sourcecode/%d.c /home/sonny/code/%s/' %(j,i)


        os.system(m)





