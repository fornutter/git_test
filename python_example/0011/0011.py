# 敏感词屏蔽

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

	if str in ListWord:
		print("Freedom")
	else:
		print("Human Rights")


if __name__ == "__main__":

	yourWord=input("please input your word：")

	fi=open_file("filtered_words.txt")

	decide(yourWord,fi)





