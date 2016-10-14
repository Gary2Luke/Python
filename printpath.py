#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# path=os.getcwd()
# path=path.replace('\\','/')
# path=raw_input('Please input path:\n')
path='/usr/bin/firefox'

# type='current ar archive'         #static library
g = file('chuli.txt', 'w')
executable = file('executable.txt', 'w')
library = file('library.txt', 'w')
for fpathe, dirs, fs in os.walk(path):
    for f in fs:
        newpath = os.path.join(fpathe, f)
        g.truncate()
        m = 'file %s >> chuli.txt' % newpath
        os.system(m)
        gg = file('chuli.txt', 'r')
        try:
            info = gg.readlines()[0]

            if 'ELF 64-bit LSB shared object' in info:
                print >> library, newpath
            elif 'ELF 64-bit LSB executable' in info:
                print >> executable,newpath
        except:
            pass
print 'ok!!!!!!!!'


