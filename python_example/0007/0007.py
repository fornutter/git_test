# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:36:35 2019

第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。

@author: as us
"""
import sys
sys.path.append(r"D:\git_test\python_example")
from fun_os import get_fixed_type_fileaname

def analyze_code(name):
    total_line=0
    blank_line=0
    comment_line=0
    code_line=0
    h=0
    a=[]
    
    g=open('D:/git_test/python_example/0007/'+name,encoding="utf-8")
    file=g.readlines()
    total_line=len(file)
    for i in file:
             if i.startswith("#"):
                comment_line+=1
             elif i=="\n":
                 blank_line+=1
             elif i.startswith("'''") or i.endswith("'''\n")or i.startswith('"""')or i.endswith('"""\n'):
                 a.append(file.index(i))
                 
            
    if len(a)>0:
        for i in range(int(len(a)/2)):
            h=a[2*i+1]-a[2*i]+1+h
    comment_line=comment_line+h
    code_line=total_line-comment_line-blank_line
        
    g.close()
    return (total_line,code_line,comment_line,blank_line)
       
                             

if __name__ == "__main__":
    
    path="D:/git_test/python_example/0007"

    a=get_fixed_type_fileaname(path,"py") 
   
    for i in a:
        b=analyze_code(i)
        print("file name is "+i)
        print('total_line:',b[0])
        print('code_line:',b[1])
        print('comment_line:',b[2])
        print('blank_line:',b[3])
        print("\n")





