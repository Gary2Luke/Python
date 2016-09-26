#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

a='rm -rf /home/sonny/static_test/*'
os.system(a)
for j in range(40,50):

    i=str(j).rjust(3, '0')

    k='/home/sonny/sourcecode/%d.c' %j
    if os.path.exists(k):



        # m='gcc -w -o /home/sonny/code/%s/%d /home/sonny/code/%s/%d.c /home/sonny/code/009/conio.c -lm' %(i,j,i,j)
        n='gcc -w -static -o /home/sonny/static_test/%d /home/sonny/sourcecode/%d.c /home/sonny/code/009/conio.c' %(j,j)

        # os.system(m)
        os.system(n)
for j in range(40,50):

    k='/home/sonny/static_test/%d' %j

    if os.path.exists(k):


        m='/home/sonny/static_test/%d' %j

        print '************%d*************' %j
        os_system = os.system(m)
        print '\n'






