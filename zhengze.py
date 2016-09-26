#!/usr/bin/python
# coding = UFT-8
import re
# from collections import Counter
# file_cnt = 0
lib_cnt = {}

file = open("/home/sonny/1.txt")
lines = file.readlines()
for line in lines:
# 	match = re.match(".*:", line)
# 	if(match):
# 		#print(line)
# 		file_cnt += 1
# 		continue

	match = re.match("\s*(.*)\s*=>\s*(.*)\s*(\(.*\))", line)
	# lib_path = ""
	if(match):
		if(match.group(2) == ""):
			lib_path = match.group(1)
		else:
			lib_path = match.group(2)
		if(lib_path not in lib_cnt):
			lib_cnt[lib_path] = 1
		else:
			lib_cnt[lib_path] += 1

# for lib in lib_cnt:
# 	print("%s\t\t%d" % (lib, lib_cnt[lib]))
#  b=Counter(lib_cnt)
b=lib_cnt
d=sorted(b.iteritems(), key=lambda t: t[1], reverse=True)

for x in d:
    print x

