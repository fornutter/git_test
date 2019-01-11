# -*- coding: utf-8 -*-
"""
将自己写的一些os有关函数保存起来，做一个自己的小封存

@author: as us
"""
import os,re

def get_fixed_type_fileaname(path,t):    
    
    #得到特定目录下的特定文件类型的文件名字，并以列表的形式产生当前目录下的该类型文件，t可以是元祖也可是字符也可是列表
    container=[]
    isString = isinstance(t, str)
    all_files_flodes=os.listdir(path)
    for i in all_files_flodes:
        if isString:
            a=re.match(r'\w*\.'+t,i)
        else:
            b="|".join(t)
            a=re.match(r'\w*\.[%s]'%b,i)
        if a:
           container.append(i)
    return(container)