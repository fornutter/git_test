# -*- coding: utf-8 -*-
"""

通过正则表达式操作将文件中空格，回车，逗号，点号替换为空格，然后通过字符串的分割方法，将其变为单词列表，然后将类别进行不重复无序化操作set（），
最后用列表的count命令进行计数，最终将其保存在字典数据中
Created on Wed Jan  9 16:19:01 2019

@author: fornut
"""

import re #导入正则表达式模块
file=open('text.txt','r')#打开文件只读模式
fole2=file.read()#整体读入文件，这个可能要后期改进
calculation={}#创建存放计数形式的键值对
change1=re.sub(r'\-\n|\n\-',"",fole2)#防止文件中出现字母没有打完就换行的情况，使其仍然是一个单词，主次此种方法返回的仍然为字符串类型
change2=re.sub(r'[\s\n\,\.]+',' ',change1)#将文中可能出现的标记符号全部用空格代替
change3=re.split(" ",change2)#将字符串以空格为界限，变换为单词的列表
for i in set(change3): #set方法相当于创建不重复的无序的列表
    calculation[i]=change3.count(i)#此处调用了列表的count方法
#在文件写入是，只有数字和字符串类型才能被写入文件，此种方法为将字典写入文件中，值得学习。
with open('result.txt','w') as result_file:
    for key,value in calculation.items():
        result_file.write(key+':'+str(value)+'\n')
file.close()