#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""串口GUI构造文件"""

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import configurationfile
import serialctl

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

class ApplicationGuiBuild(tk.Frame):
    """Build UI class."""
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=W + E + N + S)  # 上北north、下南south、左西west、右东east
        # 头标签
        self.create_label(self.master, configurationfile.row_text_1, 60, tk.W, 4, 0, 0)
        # 串口下拉选择列表
        self.create_label(self.master, "串口号", 5, tk.W+tk.N+tk.E, None, 1, 0)
        self.create_combobox_com(self.master, serialctl.SerialControl.get_serial_number(self), 45, tk.W, None, 1, 1)
        #波特率下拉列表选择
        self.create_label(self.master, "波特率", 5, tk.W + tk.N + tk.E, None, 2, 0)
        self.create_combobox_com(self.master, serialctl.SerialControl.get_serial_number(self), 45, tk.W, None, 2, 1)



    def create_label(self, frame, text , width, sticky, columnspan, rowx, columny):
        '标签，传递参数依次为frame名称，显示字符串文本，占用宽度，跨几列，坐标x，坐标y'
        Label(frame, text=text, bg="gray", fg="white", width=width).grid(row=rowx, column=columny, sticky=sticky, columnspan=columnspan)

    def create_combobox_com(self, frame, boxchoicename, width, sticky, columnspan, rowx, columny):
        '串口下拉列表，传递参数依次为frame名称，显示字符串文本，占用宽度，跨几列，坐标x，坐标y'
        self.boxValue = tk.StringVar()
        boxChoice = ttk.Combobox(frame, textvariable=self.boxValue, state='readonly',width=width)
        boxChoice['value'] = boxchoicename  #('COM1', 'COM2', 'COM3', 'COM4')
        boxChoice.current(0)
        boxChoice.bind('<<ComboboxSelected>>', self.Choice)
        boxChoice.grid(row=rowx, column=columny, sticky=sticky, columnspan=columnspan)

    def Choice(self, event):
        context = self.boxValue.get()
        com_list = serialctl.SerialControl.get_serial_number(self)
        list_com = []
        for index in range(len(com_list)):
            list_com.append(str(com_list[index]))
        if context in list_com:
            self.port = list_com.index(context)
            serialctl.SerialControl.initialization_serial_port(str(self.port))




if __name__=="__main__":
    root = tk.Tk()  #构建主窗体
    root.title("Simple Serial Port Assistant V0.0")     # 标题
    root.geometry('408x400+400+100')        # 默认窗体大小
    # Tab Control introduced here --------------------------------------
    tabControl = ttk.Notebook(root)  # Create Tab Control
    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='串口助手')  # Add the tab
    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='第二页')  # Make second tab visible
    tab3 = ttk.Frame(tabControl)  # Add a third tab
    tabControl.add(tab3, text='第三页')  # Make second tab visible
    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    app1 = ApplicationGuiBuild(tab1) #主应用窗体构建在第一页

    root.mainloop()