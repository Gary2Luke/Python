#!/usr/bin/python
# coding = UFT-8




with open('/home/sonny/2.txt', 'rb') as f:
    s = f.read()

with open('/home/sonny/33.txt', 'wb') as g:
    # g.write(s.replace("(", ""))
    s=s.replace("(", "")
    s=s.replace(")", "")
    g.write(s)


