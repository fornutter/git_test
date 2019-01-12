from urllib import request
import re

def get_pic():
  web = request.urlopen(r'http://tieba.baidu.com/p/2166231880')
  page = web.read()
  page = page.decode()

  regex = re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>')
  pic = re.findall(regex, page)
  return pic

def save(save_pic):
 path = 'D:/git_test/python_example/0013'
 count = 0
 for pic in save_pic:
     request.urlretrieve(pic, '%s/%s.jpg' % (path, count))
     count += 1

pic = get_pic()
save(pic)
