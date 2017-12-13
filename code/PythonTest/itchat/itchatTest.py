#coding=utf8
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
#itchat.auto_login()
itchat.auto_login(hotReload=True)	#Not login every time
itchat.run()