##**第 0010 题：** 使用 Python 生成类似于下图中的**字母验证码图片**

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import string, random


def get_font(num):

	return(random.sample(string.ascii_letters,num))
def get_col():

	return((random.randint(30,100),random.randint(30,100),random.randint(30,100)))




img=Image.new('RGB',(240,60),(120,120,120))
font=ImageFont.truetype("ahronbd.ttf",40)
draw=ImageDraw.Draw(img)

code=get_font(4)

for i in range(len(code)):
	draw.text((60*i+random.randint(10,16),random.randint(10,18)),code[i],font=font,fill=get_col())
for y in range(random.randint(2500,4000)):
    draw.point((random.randint(0,240), random.randint(0,60)), fill=get_col())

img = img.filter(ImageFilter.BLUR)

img.save("".join(code) + '.jpg', 'jpeg');
