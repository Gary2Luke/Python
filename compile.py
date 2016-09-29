#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
# a='rm -rf /home/sonny/static_test/*'
# os.system(a)
for j in range(1,210):

    i=str(j).rjust(3, '0')

    k='/home/sonny/code/%s/%d.c' %(i,j)
    if os.path.exists(k):



        m='gcc -w -o /home/sonny/code/%s/%d /home/sonny/code/%s/%d.c /home/sonny/code/009/conio.c -lm' %(i,j,i,j)
        n='gcc -w -static -o /home/sonny/code/%s/%d_static /home/sonny/code/%s/%d.c /home/sonny/code/009/conio.c -lm' %(i,j,i,j)

        os.system(m)
        os.system(n)






