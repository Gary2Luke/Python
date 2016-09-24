#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(1,221):
    i=str(j).rjust(3, '0')
    k='/home/sonny/code/%s/%d_static' %(i,j)
    h='/home/sonny/code/%s/%d' % (i,j)
    if os.path.exists(k):

        os.rename(k, h)
        m='cp /home/sonny/code/%s/%d /home/sonny/static_test/' %(i,j)


        os.system(m)





