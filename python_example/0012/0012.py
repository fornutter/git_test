# 敏感词屏蔽
#第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
import string
def open_file(name):
	b=[]
	with open(name,"r") as f:
		f=f.readlines()
		for i in f:
			i=i.strip()
			b.append(i)
	return b
def decide(str,ListWord):

	for i in ListWord:
		if i in str:
			str=str.replace(i,"*"*len(i))
	return str
if __name__ == "__main__":
	yourWord=input("please input your word：")

	fi=open_file("filtered_words.txt")
	print(decide(yourWord,fi))







