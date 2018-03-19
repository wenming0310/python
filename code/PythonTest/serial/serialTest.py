#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading, time, serial
#from tkinter import *
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports


# 由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

            # ===================================================================
def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class ApplicationUIBuild(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        time.sleep(1)

        # bulidButtonClick按键点击事件
        def checkButtonClick():
            port_list = list(serial.tools.list_ports.comports())
            lenport_list = len(port_list)
            if lenport_list <= 0:
                inputLogWindow.insert("The Serial port can't find!")
            else:
                for i in range(0, len(port_list)):
                    inputLogWindow.insert(tk.END, port_list[i])
                    inputLogWindow.insert(tk.END, '\n')
                    inputLogWindow.see(tk.END)
                    # print(port_list)
        # ClearButtomClick清除按键点击事件
        def ClearButtomClick():
            inputLogWindow.delete(0.0, tk.END)
        # 按键生成
        frameButton = ttk.Frame(self.master)
        frameButton.pack(fill=tk.X)
        checkButton = tk.Button(frameButton, text="生成!", width=15, command=checkButtonClick)
        checkButton.pack(fill=tk.BOTH, side=tk.LEFT, padx=11, pady=11)
        # Log窗口
        frameLogWindow = tk.Frame(self.master)
        frameLogWindow.pack(fill=tk.BOTH, expand=1)
        tk.Label(frameLogWindow, text="测试信息打印窗口:", bg="gray", fg="white", width=15).pack(fill=tk.X)
        clearButton = tk.Button(frameLogWindow, text="清除打印信息!", command=ClearButtomClick).pack(fill=tk.X)
        inputLogWindow = tk.Text(frameLogWindow)
        inputLogWindow.insert('1.0', "测试信息打印窗口\n")
        inputLogWindow.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)


# ======================
# Start GUI
# ======================
if __name__=="__main__":
    # 标题
    app = tk.Tk()
    app.title("串口助手")
    app.geometry('470x320+400+100')  # 默认窗体大小
    sloveapp = ApplicationUIBuild(app)
    app.mainloop()