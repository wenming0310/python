from aip import AipSpeech

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

