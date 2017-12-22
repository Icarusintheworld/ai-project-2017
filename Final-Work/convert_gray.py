import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pylab
import os
from PIL import Image

images = os.listdir("d:/data/JPEGImages")
for index in images:
    im = Image.open('d:/data/JPEGImages/' + index).convert('L')
    im = im.resize((512,512))
    im.save('d:/data/gray/' + index)