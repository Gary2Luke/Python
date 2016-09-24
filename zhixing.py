#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for j in range(30,40):

    k='/home/sonny/static_test/%d' %j

    if os.path.exists(k):


        m='/home/sonny/static_test/%d' %j

        print '************%d*************' %j
        os_system = os.system(m)
        print '\n'






