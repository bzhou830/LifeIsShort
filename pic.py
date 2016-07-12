#!/usr/bin/env python
# coding=utf-8

from PIL import Image
from pylab import *

im = array(Image.open('/home/robin/Pictures/tt.bmp').convert('L'))

print im

figure()

gray()

imshow(im)
#plot(im, origin='image')
#contour(im, origin='image')

axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
grid(True)
show()



#im2.save('/home/robin/blur.jpg')



