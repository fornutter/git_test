# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:29:25 2019

@author: as us
"""

import sys
sys.path.append(r"D:\git_test\python_example")
from fun_os import get_fixed_type_fileaname

def open_file(name):
    with open("D:/git_test/python_example/0007/"+name,'r') as f:
        f= f.readlines()
    return f


'''def analyze_code(name):
    total_line=0
    comment_line=0
    blank_line=0
    code_line=0
    f=open("D:/git_test/python_example/0007/"+name,'r') 
    
    f=f.readlines()
    print(type(f))
    total_line=len(f)
    for i in f:
        if i.startswith('#'):
              comment_line+=1
        elif i=="\n":
              blank_line+=1
    f.close()
    print(total_line)
    '''
if __name__ == "__main__":
    path="D:/git_test/python_example/0007"
    a=get_fixed_type_fileaname(path,"py") 
    print(open_file(a[0]))
                            