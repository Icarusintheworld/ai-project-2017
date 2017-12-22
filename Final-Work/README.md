### Introduction
__zip File__<br> 
gray.zip      处理好的图片集，灰度图，大小均为512*512<br> 

__File__<br> 
JPEGImages    原图片数据集[source](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html)<br> 
selec         原下载的数据中提供的标注集，提取了六类的相关txt<br> 
select.txt    对6类trainval.txt的合并及过滤后的文档，格式：图片名+标注<br> 

__Code__<br> 
convert_gray.py   处理图片的代码<br> 
filter.py         过滤重复标注文档的代码<br> 
input.py          进行Xtrain，Ytrain输入的代码，其中Xtrain得到的是numpy转换的矩阵，Ytrain是对应图片的label<br> 

（注：图片因为比较大我就不上传了）
