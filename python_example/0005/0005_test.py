# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:18:48 2019

@author: as us
"""
def max_num(a,b):
    if a>=b:
        return a
    else:
        return b


from PIL import Image
import os, re
pw,ph=(1136,640)
a=os.listdir("D:/git_test/python_example/0005/picture")

for i in a:
    if re.search(r"\w*\.[jpg|png]",i): #此处采用的是正则表达式判断，无需打开文件，我感觉速度可能会快
        img=Image.open("D:/git_test/python_example/0005/picture/"+i) #python中写地址斜杠问题需要注意一下
        w,h=img.size        
        w_r=w/pw
        w_h=h/ph
        c=max_num(w_r,w_h)
        if c>1:  
            img=img.resize((int(w/c),int(h/c)))#此处必须给img赋值，要不然保存的应然是 img原来图像
        img.save("D:/git_test/python_example/0005/changed_picture/"+i)
      
        