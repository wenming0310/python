#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading, time, serial
#from tkinter import *
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

class GUI(tk.Frame):
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        # 串口设置相关变量
        self.port = '0'
        self.baudrate = 115200
        # 串口号提示
        self.lab1 = tk.Label(frame, text='Serial Number')
        self.lab1.grid(row=0, column=0, sticky=tk.W)
        # 串口号选择下拉菜单
        self.boxValue = tk.StringVar()
        self.boxChoice = ttk.Combobox(frame, textvariable=self.boxValue, state='readonly')
        self.boxChoice['value'] = ('COM1', 'COM2', 'COM3', 'COM4')
        self.boxChoice.current(0)
        self.boxChoice.bind('<<ComboboxSelected>>', self.Choice)
        self.boxChoice.grid(row=1, column=0, sticky=tk.W)
        # 波特率选择提示
        self.lab2 = tk.Label(frame, text='Baudrate Set')
        self.lab2.grid(row=2, column=0, sticky=tk.W)
        # 波特率选择下拉菜单
        self.boxValueBaudrate = tk.IntVar()
        self.BaudrateChoice = ttk.Combobox(frame, textvariable=self.boxValueBaudrate, state='readonly')
        self.BaudrateChoice['value'] = (9600, 115200)
        self.BaudrateChoice.current(0)
        self.BaudrateChoice.bind('<<ComboboxSelected>>', self.ChoiceBaudrate)
        self.BaudrateChoice.grid(row=3, column=0, sticky=tk.W)
        # 输出框提示
        self.lab3 = tk.Label(frame, text='Message Show')
        self.lab3.grid(row=0, column=1, sticky=tk.W)
        # 输出框
        self.show = tk.Text(frame, width=40, height=5, wrap=tk.WORD)
        self.show.grid(row=1, column=1, rowspan=4, sticky=tk.W)
        # 输入框提示
        self.lab4 = tk.Label(frame, text='Input here,please!')
        self.lab4.grid(row=5, column=1, sticky=tk.W)
        # 输入框
        self.input = tk.Entry(frame, width=40)
        self.input.grid(row=6, column=1, rowspan=4, sticky=tk.W)
        # 输入按钮
        self.button1 = tk.Button(frame, text="Input", command=self.Submit)
        self.button1.grid(row=11, column=1, sticky=tk.E)
        # 串口开启按钮
        self.button2 = tk.Button(frame, text='Open Serial', command=self.open)
        self.button2.grid(row=7, column=0, sticky=tk.W)
        # 串口关闭按钮
        self.button3 = tk.Button(frame, text='Close Serial', command=self.close)
        self.button3.grid(row=10, column=0, sticky=tk.W)
        # 串口信息提示框
        self.showSerial = tk.Text(frame, width=20, height=2, wrap=tk.WORD)
        self.showSerial.grid(row=12, column=0, sticky=tk.W)
        # 串口初始化配置
        self.ser = serial.Serial()
        self.ser.setPort(self.port)
        # self.ser.setBaudrate(self.baudrate)
        # self.ser.open()
        # print self.ser.isOpen()
        # print self.ser
    def Choice(self, event):
        context = self.boxValue.get()
        list = ["COM1", 'COM2', 'COM3', 'COM4']
        # port_list = serial.tools.list_ports.comports()
        # for i in range(0, len(port_list)):
        #     print(port_list[i])
        #     list[i] = port_list[i]
        #     print(list[i])
        if context in list:
            self.port = list.index(context)
            # print(self.port)
            self.ser.setPort(str(self.port))

    def ChoiceBaudrate(self, event):
        self.baudrate = self.boxValueBaudrate.get()
        self.ser.setBaudrate(self.baudrate)
        print(self.baudrate)

    def Submit(self):
        context1 = self.input.get()
        n = self.ser.write(context1)
        output = self.ser.read(n)
        print(output)
        self.show.delete(0.0, tk.END)
        self.show.insert(0.0, output)

    def open(self):
        self.ser.open()
        if self.ser.isOpen() == True:
            self.showSerial.delete(0.0, tk.END)
            self.showSerial.insert(0.0, "Serial has been opend!")

    def close(self):
        self.ser.close()
        if self.ser.isOpen() == False:
            self.showSerial.delete(0.0, tk.END)
            self.showSerial.insert(0.0, "Serial has been closed!")

root = tk.Tk()
root.title("Serial GUI")
# root.geometry("3000x4000")
app = GUI(root)
root.mainloop()

"""
#标题
app = tk.Tk()
app.title("串口助手")
app.geometry('470x320+400+100')     #默认窗体大小

#bulidButtonClick按键点击事件
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
    #print(port_list)
#按键生成
frameButton = ttk.Frame(app)
frameButton.pack(fill=tk.X)
checkButton = tk.Button(frameButton, text = "生成!", width = 15, command = checkButtonClick)
checkButton.pack(fill=tk.BOTH, side=tk.LEFT,padx = 11, pady = 11)

#ClearButtomClick清除按键点击事件
def ClearButtomClick():
    inputLogWindow.delete(0.0,tk.END)
#Log窗口
frameLogWindow = tk.Frame(app)
frameLogWindow.pack(fill=tk.BOTH, expand = 1)
tk.Label(frameLogWindow, text = "测试信息打印窗口:", bg = "gray", fg = "white", width = 15).pack(fill=tk.X)
clearButton = tk.Button(frameLogWindow, text = "清除打印信息!", command = ClearButtomClick).pack(fill=tk.X)
inputLogWindow = tk.Text(frameLogWindow)
inputLogWindow.insert('1.0',"测试信息打印窗口\n")
inputLogWindow.pack(fill=tk.BOTH,side=tk.LEFT,expand = 1)

# ======================
# Start GUI
# ======================
app.mainloop()
"""