# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 13:48:39 2019

@author: as us
"""

from PIL import Image, ImageDraw, ImageFont

def picture_number(img,num):
    im=ImageDraw.Draw(img)
    numFont=ImageFont.truetype("ahronbd.ttf",200)
    im.text((300,-50),num,fill=(255,255,1),font=numFont)
    img.save("123.jpg")
    img.show()

img=Image.open("wechat.jpg")
picture_number(img,"100")