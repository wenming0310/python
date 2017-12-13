#coding=utf8
import requests

apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key'	: 'b7ac5505add541918f2796561fa874f5',# Tuling Key
    'info'	: 'hello',#Send message
    'userid'	: 'wechat-robot',#User id (no limit)
}
#one post request
r = requests.post(apiUrl, data=data).json()
#print return value
print(r)
