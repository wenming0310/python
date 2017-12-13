<<<<<<< HEAD
#coding=utf8
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
#itchat.auto_login()
itchat.auto_login(hotReload=True)	#Not login every time
=======
#coding=utf8
import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])
#itchat.auto_login()
itchat.auto_login(hotReload=True)	#Not login every time
>>>>>>> 228d57760e22242bd39aba4b7829a3e0c41dd95d
itchat.run()