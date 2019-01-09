#coding:utf-8

"""第0001题：做为Apple Store App独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用Python如何生成200个激活码（或者优惠券）？"""




'''
#原来作者的写法
import uuid

def get_id(num):
    list_id = []
    for i in range(num):
        id = str(uuid.uuid1()).replace('-','')
        list_id.append(id)
    return list_id
id = get_id(200)
with open("file_id.txt","w") as file:
    for i in id:
        file.write(i+"\n")
'''
import random, string

def get_code(num,length):
    #使用的是random.choice 方法
    nut=''
    char=string.ascii_letters+string.digits #此为string 模块里的属性值，
    c=[]
    for i in range(num):
        b=0        
        nut=''
        while b<length:
            a=random.choice(char)
            nut=nut+a
            b=b+1
        c.append(nut)
    print(c)
get_code(100,7)

def get_code2(num,length):
    no_space=''
    jian="\n"
    #此处应用random.smmple 方法，简单计算，但是random .sample 方法返回的是一个列表对象，需要用join 方法将其合并成字符串
    char=string.ascii_letters+string.digits
    c=[]
    for i in range(num):
        a=no_space.join(random.sample(char,length))#其中通过“”直接调用str的join 方法
        c.append(a)
    d=jian.join(c)#此处join的好用法是回车的符号，作为连接起来的间隔符号
    print(d)
get_code2(100,8)

def get_code3(num,length):
    # 通过读写文件
    no_space=''
    jian="\n"
    #此处应用random.smmple 方法，简单计算，但是random .sample 方法返回的是一个列表对象，需要用join 方法将其合并成字符串
    char=string.ascii_letters+string.digits
    c=[]
    for i in range(num):
        a=no_space.join(random.sample(char,length))#其中通过“”直接调用str的join 方法
        c.append(a)
    d=jian.join(c)#此处join的好用法是回车的符号，作为连接起来的间隔符号
    with open('Activation_code.txt', 'w') as f:
        f.write(d)
get_code3(200,7)