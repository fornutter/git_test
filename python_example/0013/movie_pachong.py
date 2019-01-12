from urllib import request
import re
def getHtml(path):

    open_web=request.urlopen(web)
    open_web=open_web.read().decode('utf-8')
    return open_web


def getImg(html):

    name=re.compile(r'http.*\.jpg')

    all_url=re.findall(name,html)
    count = 0
    for i in all_url:
        local_path='D:/git_test/python_example/0013/movie'
        request.urlretrieve(i,"%s/%s.jpg"%(local_path,count))
        count+=1

web = "https://movie.douban.com/top250"


html=getHtml(web)

getImg(html)