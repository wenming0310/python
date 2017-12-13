'''
__author__ = 'zwm'
# -*-coding: UTF-8 -*-

from tkinter import *       #导入tkinter库的所有类这样在引用时就不需要前面加tkinter.前缀了

root = Tk()                   #创建窗口对象的背景色
'''

# -*- coding:utf-8 -*-
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import tkinter.messagebox as tkMessageBox
import os
import os.path


def exit_window(root):
    """close the main window"""
    root.destroy()


def show_info():
    """show the software info"""
    tkMessageBox.showinfo("About",
                          """ 
         Linux Command Manual 
    ------------------------------------------ 
        version: 1.0 
        author: Cullen 
        Email:  wangyiyan402@163.com 
    ------------------------------------------""")


def show_help():
    """show help info"""
    tkMessageBox.showinfo("help",
                          """ 
             Linux & Autotest Command Manual 
    ----------------------------------------------------------------- 
    1.鼠标或键盘箭头移动到所要查看的命令，回车即可在右恻查看命 
    令帮助文档. 
    2.搜索框内可直接输入要查询的命令，回车或点击搜索图标均可. 
    3.如果有新命令文档需要添加，请将文档信息以txt格式，编码选择 
    utf-8保存到doc文件夹下. 
    ------------------------------------------------------------------""")


def get_cmd_list(dir):
    """this function will walk the given dir path
    and return a list contains all filename under this path in order"""

    if not os.path.exists(dir):
        print
        "Path Error: No such file or directory"
        tkMessageBox.showwarning("提示", "Directory : %s not found!" % dir)
        # sys.exit(1)

    cmd_list = os.listdir(dir)
    result = []
    for item in cmd_list:
        if item.endswith('.txt'):
            result.append(item)
    result.sort()
    return result


class RightFrame():
    """create the frame include the label and Text area"""
    cmd_path = os.getcwd() + os.path.sep + 'doc\\'

    def __init__(self):
        self.frame = Frame()

#        self.image = ImageTk.PhotoImage(file=r'img\zoom.bmp')
#        self.button = Button(self.frame, image=self.image, command=self.get_entry_input)
#        self.button.pack(side=RIGHT, fill=X)

        self.entry = Entry(self.frame, bd=2, width=40, justify=RIGHT)
        self.entry.pack(side=RIGHT, fill=X)
        self.entry.bind('<Return>', self.get_input)

    def find_input(self, input, dir):
        global left_frame
        global textarea
        cmd_list = get_cmd_list(dir)
        # print cmd_list
        input += '.txt'
        file_path = dir + input

        if input not in cmd_list:
            tkMessageBox.showwarning("提示", "Command : %s not found!" % input)
            return
        index = cmd_list.index(input)
        # get the activate index
        left_frame.listbox.selection_clear(0, END)
        # active_index = left_frame.listbox.index(ACTIVE)
        # print active_index
        # #
        # print left_frame.listbox.selection_clear(active_index)

        left_frame.listbox.selection_set(index)
        # print left_frame.listbox.index(ACTIVE)

        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)

        try:
            with open(file_path, 'r') as f:
                for item in f:
                    textarea.insert(END, item)
        except IOError as e:
            # print "open cmd info error: %s" % e
            tkMessageBox.showwarning("提示", "open cmd %s: %s" % (input, e))
            self.entry.delete(0, END)

        textarea.config(state=DISABLED)

    def get_input(self, event):
        self.input = self.entry.get().strip()
        self.entry.delete(0, END)
        self.find_input(self.input, self.cmd_path)

    def get_entry_input(self):
        # print os.getcwd()
        self.input = self.entry.get().strip()
        self.find_input(self.input, self.cmd_path)


class LeftFrame():
    """create the frame which contains a listbox and scrollbar"""

    # message_ft = tkFont.Font(family="Arial", size=12)

    def __init__(self):
        self.message_ft = tkFont.Font(family="Arial", size=12)
        # self.active = ''
        self.frame = Frame()
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL, bg='green')
        self.listbox = Listbox(self.frame, bg="#D6D6D6", selectborderwidth=1, selectbackground="#1979CA",
                               font=self.message_ft, height=20, width=30)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=RIGHT, fill=BOTH, expand=1)
        self.listbox.bind('<Return>', self.show_cmd_mean)

    def show_cmd_mean(self, event):
        global textarea
        textarea.config(state=NORMAL)
        textarea.delete(1.0, END)

        # print event.widget.get(ACTIVE)
        self.active = event.widget.get(ACTIVE)
        # textarea.insert(END, self.active)


        try:
            file_path = os.getcwd() + os.path.sep + "doc\\" + self.active + '.txt'
            with open(file_path, 'r') as f:
                for item in f:
                    textarea.insert(END, item)
        except IOError as e:
            # print "open cmd info error: %s" % e
            tkMessageBox.showwarning('提示', "open cmd info error: %s" % e)

        textarea.config(state=DISABLED)


class TextFrame():
    def __init__(self):
        global textarea
        self.frame = Frame()
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        textarea = Text(self.frame, bg='#CCFFCC', width=90, height=30)
        self.scrollbar.config(command=textarea.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        textarea.config(yscrollcommand=self.scrollbar.set)
        textarea.pack(side=LEFT, fill=BOTH, expand=1)


class MyMenu():
    def __init__(self, root):
        self.menubar = Menu(root)
        self.optionmenu = Menu(self.menubar, tearoff=1)
        self.optionmenu.add_command(label='About', command=show_info)
        self.optionmenu.add_command(label='Help', command=show_help)
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label='Exit', command=lambda: exit_window(root))
        self.menubar.add_cascade(label='Options', menu=self.optionmenu)


def main():
    global textarea
    global left_frame
    root = Tk()
    root.title("Command Manual")
    root.resizable(0, 0)

    menu = MyMenu(root)
    root.config(menu=menu.menubar)
    left_frame = LeftFrame()
    left_frame.frame.grid(row=0, column=0, rowspan=2, sticky=N + W + S + E)

    right_frame = RightFrame()
    right_frame.frame.grid(row=0, column=1, sticky=N + W + E)

    # show the command list according the given path
    cmd_path = os.getcwd()
    cmd_path = cmd_path + os.path.sep + 'doc'
    cmd_list = get_cmd_list(cmd_path)

    for item in cmd_list:
        item = item.split('.')[0]
        left_frame.listbox.insert(END, item)

    text_frame = TextFrame()
    text_frame.frame.grid(row=1, column=1, sticky=N + W + S + E)

    root.mainloop()


if __name__ == '__main__':
    main()