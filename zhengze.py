#!/usr/bin/python
# coding = UFT-8
import re
import os
dynamic=[]
static=[]
file = open("/home/sonny/2222.txt")
lines = file.readlines()

for line in lines:
	match = re.match(".*:", line)
	if (match):
		a=line.split(":", 1)[0]
		# print line.split(":", 1)[0]
		k = 'cp /bin/%s /home/sonny/benchmark/library/' %a
		if 'linked' in line:
			os.system(k)
		if 'symbolic' in line:

			b = line.split(" ", )[-1]
			# print b
			m='cp %s /home/sonny/benchmark/library/' %b.replace('\n','')
			# print m
			os.system(m)
	continue
	# if "dynamically linked" in line:
	# 	dynamic.append(line)
	# if 'statically linked' in line:
	# 	static.append(line)



