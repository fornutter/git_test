# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:37:34 2019

@author: as us
"""

from PIL import *
img=Image.new("RGB",(400,400),"Black")
draw=ImageDraw.Draw(img)
draw.arc((150,150,250,250),0,180,'red')
draw.polygon(((10,10),(10,20),(20,10)),'gold','brown')
img.show()