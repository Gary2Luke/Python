#!/usr/bin/python
# coding = UFT-8
import os
out = file('lddResult.txt','w')
clear = file('chuli.txt', 'wb')

def lddResult(path):
	# path = '/usr/share/gedit'

	if os.path.isfile(path):
		n = 'ldd %s >>lddResult.txt' % path
		os.system(n)
	else:
		for fpathe, dirs, fs in os.walk(path):
			for f in fs:
				newpath = os.path.join(fpathe, f)
				mm = 'ldd %s >>lddResult.txt' % newpath
				os.system(mm)

name = 'apache2'							##!!!!!! here start

m = 'whereis %s >>chuli.txt' % name
os.system(m)
lines = file('chuli.txt', 'r')
for line in lines:

	line = line.replace('\n', '')
	line = line.split(' ')
	for i in range(1, len(line)):
		print line[i]
		lddResult(line[i])

print 'OK!!!!!'


