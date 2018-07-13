from aip import AipSpeech
import time
import pygame
import os
#import mp3play     #语速正常，但只能用于python2.7，不支持python3.x

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('你还好？我很好，请不要惦记。对不起。对不起！', 'zh', 1, {'vol': 5, 'per': 4,} )
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

file=r'D:\CC++C#Code\github\python\code\PythonTest\baidu-aip\auido.mp3'
pygame.mixer.init() # 语速失真
print("播放音乐1")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()

os.system('auido.mp3') #语速正常，缺点，弹出播放器窗口，打开完成后不占用进程
'''
def playmusic(path):
    clip = mp3play.load(path)
    clip.play()
    time.sleep(10)
    clip.stop()

playmusic('auido.mp3')
'''