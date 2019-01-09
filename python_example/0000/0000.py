# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:37:34 2019

@author: as us
"""

from PIL import Image, ImageDraw,ImageFont

def picture_num(img,num):
    im=ImageDraw.Draw(img)
    print(img.size)
    NumFont=ImageFont.truetype("ahronbd.ttf",200)
    im.text((360, -50), num,"yellow",font=NumFont)
    img.save("renew.jpg")
    img.show()
    
img=Image.open("wechat.jpg")
picture_num(img,"100")
    
