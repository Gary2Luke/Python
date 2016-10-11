#!/usr/bin/python
# coding = UFT-8
import os

path = '/home/sonny/Analyze_library/jre1.8.0_101'
out = file('lddResult.txt','w')
# out.truncate(0)
for fpathe, dirs, fs in os.walk(path):
	for f in fs:
		newpath = os.path.join(fpathe, f)
		# print >>out,newpath+':'
		m = 'ldd %s >>lddResult.txt' % newpath
		# print m
		os.system(m)
print 'OK!!!!!'

