# -*- coding: utf-8 -*-
'''
jianguojian
jiangji


'''
from collections import Counter
import os, re

def find_txt(path):
    b=[]
    all_file=os.listdir(path)
    for i in all_file:
        if re.search(r'\w*\.txt',i): #这个地方为什么不能用match  还需要探讨
            b.append(i)
    return b
def remove_meaning_word(a):#剔除无意义的单词
    b=["you","I",'me','they','we',"a",'to','the','for','in','on','near'] #有待补充
    a = [x for x in a if x.lower() not in b]
    return a
def find_all_word(f):
    change1=re.sub(r'\-\n|\n\-',"",f)#防止文件中出现字母没有打完就换行的情况，使其仍然是一个单词，主次此种方法返回的仍然为字符串类型
    change1=re.sub(r'[\s\n\,\.\:]+',' ',change1)#将文中可能出现的标记符号全部用空格代替
    change1=re.split(" ",change1)
    return change1
    

if __name__ == "__main__":
    path='D:/git_test/python_example/0006/text'
    b={}
    all_text_file=find_txt(path)
    for i in all_text_file:
        with open(path+'/'+i,"r") as f:
            f=f.read()
            change=find_all_word(f)
            change=remove_meaning_word(change)
            a=Counter(change).most_common(1)
            b[i]=a
    print(b)
