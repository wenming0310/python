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
        self.create_label(self.master, "串口助手V1.0", None, tk.W, 4, 0, 0)
        #Label(master, text=configurationfile.row_text_1, bg="gray", fg="white", width=None).grid(row=0, column=0, sticky=tk.W, columnspan=4)
        self.create_combobox(self.master, serialctl.SerialControl.get_serial_number(self))

    def create_label(self, frame, text , width, sticky, columnspan, x, y):
        '标签，传递参数依次为frame名称，显示字符串文本，占用宽度，跨几列，坐标x，坐标y'
        Label(frame, text=text, bg="gray", fg="white", width=width).grid(row=x, column=y, sticky=sticky, columnspan=columnspan)

    def create_combobox(self, frame, boxchoicename):
        '下拉列表，传递参数依次为frame名称，'
        self.boxValue = tk.StringVar()
        boxChoice = ttk.Combobox(frame, textvariable=self.boxValue, state='readonly')
        boxChoice['value'] = boxchoicename  #('COM1', 'COM2', 'COM3', 'COM4')
        boxChoice.current(0)
        boxChoice.bind('<<ComboboxSelected>>', self.Choice)
        boxChoice.grid(row=1, column=0, sticky=tk.W)

    def Choice(self, event):
        context = self.boxValue.get()
        #list = ["COM1", 'COM2', 'COM3', 'COM4']
        list = serialctl.SerialControl.get_serial_number(self)
        # port_list = serial.tools.list_ports.comports()
        # for i in range(0, len(port_list)):
        #     print(port_list[i])
        #     list[i] = port_list[i]
        #     print(list[i])
        print(context)
        print(list)
        for context in list:
            self.port = list[context]
            #print(self.port)
            self.ser.setPort(str(self.port))


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