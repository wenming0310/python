'''
# from tkinter import *  #第一步
# 第二步，创建一个顶层窗口对象，来容纳整个GUI程序
# 在您的顶层窗口的对象上创建所有的GUI模块
# 把这些GUI模块与底层程序代码想连接
import os, getpass, time
import tkinter as tk

root = tk.Tk()
#top=Tkinter.Tk()#创建一个顶层窗口对象

label = tk.Label(root, text='hell world')
label.pack()
tk.mainloop()  # 进入主事件循环
'''
__author__ = 'zwm'
# -*-coding: UTF-8 -*-
'''
import os, getpass, time
import tkinter as tk

top = tk.Tk()
#进入消息循环
top.mainloop()
'''
'''
from tkinter import *       #导入tkinter库的所有类这样在引用时就不需要前面加tkinter.前缀了

root = Tk()                   #创建窗口对象的背景色
                              #创建两个列表
li  = ['C', 'Python', 'PHP', 'HTML', 'SQL', 'JAVA']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)           #创建两个列表组件
listb2 = Listbox(root)
for item in li:
    listb.insert(0,item)        #第一个组件插入数据
for item in movie:
    listb2.insert(0,item)
listb.pack()                    #将组件放置到主窗口中
listb2.pack()
root.mainloop()                 #进入消息循环
'''
import sys
import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
import itchat

KEY = 'b7ac5505add541918f2796561fa874f5'


def get_response(msg):
    # create send to server data
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,  # Tuling Key
        'info': msg,  # Send message
        'userid': 'wechat-robot',  # User id (no limit)
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # get method:if dictionary don't have 'text' value, return None, couldn't throw the error
        return r.get('text')
    # Prevent program occur abnormal exit, use try-except to catch the abnormal.
    # if the server couldn't return not-json or no contact, progran will run into return
    except:
        # will return None
        return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # Set a default answer when the tuling key have the issue.
    defaultReply = 'I received: ' + msg['Text']
    # If the tuling key go wrong, the reply is None
    reply = get_response(msg['Text'])
    itchat.send(reply, 'filehelper')
    # a or b means if a is content so return a else return None.
    # is content means not empty or not None, you can test use 'if a: print('True')'
    return reply or defaultReply


def initfunction():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = QtTest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def startrobot():
    # KEY = QtTest.Ui_MainWindow.lineEdit_key('Text')
    # apiUrl =  QtTest.Ui_MainWindow.lineEdit_addr('Text')
    # use hot reload
    itchat.auto_login(hotReload=True)
    itchat.run()
def closerobot():
    sys.exit(1)
    itchat.logout
    QtTest.MainWindow.close



if __name__ == '__main__':
    initfunction()
