#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 数据筛选之后，进行导入模型的预处理

# 步骤
# 1.读入select.txt
# 2.根据txt的name找到Image中的图片
# 3.导入图片并将其以矩阵形式存入Xtrain
# 4.根据txt的label存入对应的Ytrain

import os
import re
from PIL import Image
import pylab
import numpy as np

images = os.listdir("d:/data/gray")
for name in images:
	images[images.index(name)]=name[:-4]

with open('select.txt','r') as fp:
	for line in fp.readlines():
		name, value= line.split()
		if str(name) in images:
			filename = 'd:/data/gray/'+str(name)+'.jpg'
			#print(filename)
			X_train = np.asarray(Image.open(filename))
			Y_train = value




