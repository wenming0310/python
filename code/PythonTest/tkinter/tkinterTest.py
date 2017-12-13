#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()

'''
# ipadx设置内部间隙
# padx设置外部间隙
# -*- coding: cp936 -*-
# 不设置root的大小，使用默认
from tkinter import *
root = Tk()
# 改变root的大小为80x80
# root.geometry('80x80+0+0')
print(root.pack_slaves())
# 创建三个Label分别使用不同的fill属性,改为水平放置
# 将第一个LabelFrame居左放置
L1 = LabelFrame(root,text = 'pack1',bg = 'red')
# 设置ipadx属性为20
L1.pack(side = LEFT,ipadx = 20)
Label(L1,
      text = 'inside',
      bg = 'blue'
      ).pack(expand = 1,side = LEFT)
L2 = Label(root,
           text = 'pack2',
           bg = 'blue'
           ).pack(fill = BOTH,expand = 1,side = LEFT,padx = 10)
L3 = Label(root,
           text = 'pack3',
           bg = 'green'
           ).pack(fill = X,expand = 0,side = LEFT,pady = 10)
print(root.pack_slaves())
root.mainloop()
'''
