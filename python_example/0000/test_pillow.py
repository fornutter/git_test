# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:16:16 2019

@author: as us
"""

from PIL import Image
im=Image.new("RGB",(400,400),"red")
#im.show()

im2=Image.open("wechat.jpg")
#im2.show()
im2.convert("CMYK")
print(im2.mode)
#im.save("redsqure.jpg")