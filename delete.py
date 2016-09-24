#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(1,221):
    i = str(j).rjust(3, '0')
    k='/home/sonny/static_test/%d' %j

    if not os.path.exists(k):


        m='rm -rf /home/sonny/code/%s' %i


        os.system(m)






