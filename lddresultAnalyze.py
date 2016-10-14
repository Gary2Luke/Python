#!/usr/bin/python
# coding = UFT-8
import re
from collections import Counter

lib_cnt = {}

out= file('apache2_library.txt','w')
gg = file("lddResult.txt",'r')
for line in gg.readlines():
	match = re.match(".*:", line)
	if(match):
		# print(line)

		continue

	match = re.match("\s*(.*)\s*=>\s*(.*)\s*(\(.*\))", line) 		#  '.'match all except '\n'

	if(match):
		if(match.group(2) == ""):
			lib_path = match.group(1)
		else:
			lib_path = match.group(2)
		if(lib_path not in lib_cnt):
			lib_cnt[lib_path] = 1
		else:
			lib_cnt[lib_path] += 1
# sortresult = sorted(lib_cnt.items(), key=lambda x:x[1], reverse=True)  		#sort

for item in sorted(lib_cnt.items(), key=lambda x:x[1], reverse=True):
	item = str(item)
	item = item.replace('(','')
	item = item.replace(')','')
	print >> out, item


