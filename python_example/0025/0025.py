from aip import AipSpeech

APP_ID = ''
API_KEY = ''
SECRET_KEY = ""

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



#将文字直接输出成音频文件

# result  = client.synthesis('你好百度', 'zh', 1, {
#     'vol': 5,
# })

# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)

# 将音频文件直接识别为文字

# # 读取文件
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# # 识别本地文件
# client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
#     'dev_pid': 1536,
# })

#可参考的文档

#http://ai.baidu.com/docs#/ASR-Online-Python-SDK/top