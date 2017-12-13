<<<<<<< HEAD
#coding=utf8
import requests
import itchat

KEY = 'b7ac5505add541918f2796561fa874f5'

def get_response(msg):
    #create send to server data
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
    'key'	: KEY,# Tuling Key
    'info'	: msg,#Send message
    'userid'	: 'wechat-robot',#User id (no limit)
    }
    try:
        r = requests.post(apiUrl, data=data).json()
    #get method:if dictionary don't have 'text' value, return None, couldn't throw the error
        return r.get('text')
    #Prevent program occur abnormal exit, use try-except to catch the abnormal.
    #if the server couldn't return not-json or no contact, progran will run into return
    except:
	#will return None
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    #Set a default answer when the tuling key have the issue.
    defaultReply = 'I received: ' + msg['Text']
    #If the tuling key go wrong, the reply is None
    reply = get_response(msg['Text'])
    itchat.send(reply, 'filehelper')
    #a or b means if a is content so return a else return None.
    #is content means not empty or not None, you can test use 'if a: print('True')'
    return reply or defaultReply

#use hot reload
itchat.auto_login(hotReload=True)
itchat.run(True)
=======
#coding=utf8
import requests
import itchat

KEY = 'b7ac5505add541918f2796561fa874f5'

def get_response(msg):
    #create send to server data
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
    'key'	: KEY,# Tuling Key
    'info'	: msg,#Send message
    'userid'	: 'wechat-robot',#User id (no limit)
    }
    try:
        r = requests.post(apiUrl, data=data).json()
    #get method:if dictionary don't have 'text' value, return None, couldn't throw the error
        return r.get('text')
    #Prevent program occur abnormal exit, use try-except to catch the abnormal.
    #if the server couldn't return not-json or no contact, progran will run into return
    except:
	#will return None
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    #Set a default answer when the tuling key have the issue.
    defaultReply = 'I received: ' + msg['Text']
    #If the tuling key go wrong, the reply is None
    reply = get_response(msg['Text'])
    itchat.send(reply, 'filehelper')
    #a or b means if a is content so return a else return None.
    #is content means not empty or not None, you can test use 'if a: print('True')'
    return reply or defaultReply

#use hot reload
itchat.auto_login(hotReload=True)
itchat.run(True)
>>>>>>> 228d57760e22242bd39aba4b7829a3e0c41dd95d
