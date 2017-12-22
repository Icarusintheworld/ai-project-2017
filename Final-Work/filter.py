#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 对输入的标注进行去重处理
import os
import sys
#import numpy as np

def init(filename):
	tmp = {}	#一个字典
	for line in filename.readlines():
		name,label = line.split()
		if tmp.__contains__(name):
			if label > str(-1):
				tmp[name] = label
		else:
			tmp[name] = [label]
	return tmp

f1 = open('combine.txt','r')
result = init(f1)
f1.close()

with open('select.txt','w') as f2:
	for key in result:
		f2.write(key)
		for value in result[key]:
			f2.write(' ')
			f2.write(value)
		f2.write('\n')





