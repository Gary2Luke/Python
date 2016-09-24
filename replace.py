#!/usr/bin/env python
# -*- coding: utf-8 -
import os
for j in range(1,221):

    i=str(j).rjust(3, '0')
    h = '/home/sonny/code/%s/%d.C' % (i, j)
    k='/home/sonny/code/%s/%d.c' %(i,j)
    if os.path.exists(h):

        os.rename(h, k)
        with open(k,'rb') as f:
            s = f.read()

        with open(k,'wb') as g:
            g.write(s.replace("\32", ""))