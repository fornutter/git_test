
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
    code_lines = 0       #代码行数
    comment_lines = 0    #注释行数
    blank_lines = 0      #空白行数  内容为'\n',strip()后为''
    is_comment = False
    start_comment_index = 0 
    with open("D:/git_test/python_example/0007/"+name,'r',encoding='utf-8') as f:

        for index,line in enumerate(f,start=1):
            line = line.strip()
            if not is_comment:
                if line.startswith("'''") or line.startswith('"""'):
                    is_comment = True
                    start_comment_index = index
                elif line.startswith('#'):
                    comment_lines += 1
                elif line == '':
                    blank_lines += 1
                else:
                    code_lines += 1
            else:
                if line.endswith("'''") or line.endswith('"""'):
                    is_comment = False
                    comment_lines += index - start_comment_index + 1
                else:
                    pass
        return (code_lines,comment_lines,blank_lines)
                             

if __name__ == "__main__":
    
    path="D:/git_test/python_example/0007"

    a=get_fixed_type_fileaname(path,"py") 
   
    for i in a:
        b=analyze_code(i)
        print("file name is "+i)
        print('code_line:',b[0])
        print('comment_line:',b[1])
        print('blank_line:',b[2])
        print("\n")





