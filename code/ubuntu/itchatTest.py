#coding=utf8
import itchat
'''
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
#itchat.auto_login()
itchat.auto_login(hotReload=True)	#Not login every time
itchat.run()
'''

itchat.auto_login(hotReload=True)
#itchat.run()
itchat.send(u'Test message.', 'filehelper')

'''
#could run but not useful
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return msg['Text']

itchat.auto_login()
itchat.run()
'''
