# -*- coding: utf-8 -*-

import os,re


def get_all_path(path,type):

    """

    获得指定文件夹（path）下的所有的指定文件类型（type）的绝对路径

    path 为制定的文件夹的制定路径，类型为字符型

    type 为指定的文件类型，类型为列表类型，当不指定文件类型时，type请传入空列表  type中不需要带。

    返回一个列表


    """

    list_path=[]
    def get_path(path_one,list_path,type_one):
        fileDoc=[]
        fileDoc=os.listdir(path_one)
        for i  in fileDoc:
            a=os.path.join(path_one,i)
            if  not os.path.isdir(a):
                if decide_type(i,type):
                    list_path.append(a)
            else:
                get_path(a,list_path,type_one)
        return list_path
    list_path= get_path(path,list_path,type)
    return list_path






def decide_type(name,t):


    """
     判断给定的文件名，是否是给定类型的文件

     name 为文件的名称，需要包含后缀名

     t为列表类型，其中存放后缀名， 不需要带点

     返回布尔类型的值
    """


    if len(t)==0:
        return True
    elif len(t)==1:
        a=re.match(r'\w*\.'+t[0],name)
        return (a and True)
    else:
        b="|".join(t)
        a=re.match(r'\w*\.[%s]'%b,name)

        return (a and True)







def get_fixed_type_fileaname(path,t):    
    """
    得到特定目录下的特定文件类型的文件名字，
    并以列表的形式产生当前目录下的该类型文件，
    t可以是元祖也可是字符也可是列表
    """
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



def count_all_code(path,type):
    """

    统计某一路径下所有指定类型的代码总数量



    """



    all_path=[]
    one_file=()
    all_code=0
    all_path=get_all_path(path,type)
    for i in all_path :
        one_file=count_code(i)
        print("file name is :"+os.path.split(i)[1])
        print("code_lines is :%d"%one_file[0])
        print("comment_lines is :%d"%one_file[1])
        print("blank_lines is :%d"%one_file[2])
        print("total_lins is: %d\n"%sum(one_file))

        all_code+=sum(one_file)
    print(all_code)











def count_code(path):

    """
    统计给定绝对路径下的某一个文件的代码数目


    """
    code_lines = 0       #代码行数
    comment_lines = 0    #注释行数
    blank_lines = 0      #空白行数  内容为'\n',strip()后为''
    is_comment = False
    start_comment_index = 0 
    with open(path,'r',encoding='utf-8') as f:

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




