# !/usr/bin/python
# coding=utf-8
# -*- coding: UTF-8 -*-

'''
import time
import tkinter as tk


class Window:
    def __init__(self, title='nms', width=300, height=120, staFunc=bool, stoFunc=bool):
        self.w = width
        self.h = height
        self.stat = True
        self.staFunc = staFunc
        self.stoFunc = stoFunc
        self.staIco = None
        self.stoIco = None

        self.root = tk.Tk(className=title)

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def packBtn(self):
        self.btnSer = tk.Button(self.root, command=self.event, width=15, height=3)
        self.btnSer.pack(padx=20, side='left')
        btnQuit = tk.Button(self.root, text='关闭窗口', command=self.root.quit, width=15, height=3)
        btnQuit.pack(padx=20, side='right')

    def event(self):
        self.btnSer['state'] = 'disabled'
        if self.stat:
            if self.stoFunc():
                self.btnSer['text'] = '启动服务'
                self.stat = False
                self.root.iconbitmap(self.stoIco)
        else:
            if self.staFunc():
                self.btnSer['text'] = '停止服务'
                self.stat = True
                self.root.iconbitmap(self.staIco)
        self.btnSer['state'] = 'active'

    def loop(self):
        self.root.resizable(False, False)  # 禁止修改窗口大小
        self.packBtn()
        self.center()  # 窗口居中
        self.event()
        self.root.mainloop()

        ########################################################################


def sta():
    print('start.')
    return True


def sto():
    print('stop.')
    return True


if __name__ == '__main__':
    import sys, os

    w = Window(staFunc=sta, stoFunc=sto)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')
    w.loop()
'''
'''
#not work
# coding:utf-8
from tkinter import *
from scrolledtext import ScrolledText  # 文本滚动条
import threading
import time
from PIL import ImageTk, Image


def count(i):
    for k in range(1, 100 + 1):
        text.insert(END, '第' + str(i) + '线程count:  ' + str(k) + '\n')
        time.sleep(0.001)


def fun():
    for i in range(1, 5 + 1):
        th = threading.Thread(target=count, args=(i,))
        th.setDaemon(True)  # 守护线程
        th.start()
    var.set('MDZZ')


root = Tk()
root.title('九日王朝')  # 窗口标题
root.geometry('+600+100')  # 窗口呈现位置
image2 = Image.open(r'ParticleSmoke.png')
background_image = ImageTk.PhotoImage(image2)
textlabel = Label(root, image=background_image)
textlabel.grid()
text = ScrolledText(root, font=('微软雅黑', 10), fg='blue')
text.grid()
button = Button(root, text='屠龙宝刀 点击就送', font=('微软雅黑', 10), command=fun)
button.grid()
var = StringVar()  # 设置变量
label = Label(root, font=('微软雅黑', 10), fg='red', textvariable=var)
label.grid()
var.set('我不断的洗澡，油腻的师姐在哪里')
root.mainloop()
'''
'''
import tkinter,time,threading,random,queue
class GuiPart():
    def __init__(self,master,queue,endCommand):
        self.queue=queue
        tkinter.Button(master,text='Done',command=endCommand).pack()
    def processIncoming(self):
        while self.queue.qsize():
            try:
                msg=self.queue.get(0)
                print(msg)
            except queue.Empty:
                pass
class ThreadedClient():
    def __init__(self,master):
        self.master=master
        self.queue=queue.Queue()
        self.gui=GuiPart(master,self.queue,self.endApplication)
        self.running=True
        self.thread1=threading.Thread(target=self.workerThread1)
        self.thread1.start()
        self.periodicCall()
    def periodicCall(self):
        self.master.after(200,self.periodicCall)
        self.gui.processIncoming()
        if not self.running:
            self.master.destroy()
    def workerThread1(self):
        #self.ott=Tkinter.Tk()
        #self.ott.mainloop()
        while self.running:
            time.sleep(rand.random()*1.5)
            msg=rand.random()
            self.queue.put(msg)
    def endApplication(self):
        self.running=False
rand=random.Random()
root=tkinter.Tk()
client=ThreadedClient(root)
root.mainloop()
'''
'''
# coding=utf-8
import threading  # 导入threading包
from time import sleep
import time


def task1():
    print("Task 1 executed.")
    sleep(1)


def task2():
    print("Task 2 executed.")
    sleep(5)


print("多线程：")
starttime = time.time();  # 记录开始时间
threads = []  # 创建一个线程列表，用于存放需要执行的子线程
t1 = threading.Thread(target=task1)  # 创建第一个子线程，子线程的任务是调用task1函数，注意函数名后不能有（）
threads.append(t1)  # 将这个子线程添加到线程列表中
t2 = threading.Thread(target=task2)  # 创建第二个子线程
threads.append(t2)  # 将这个子线程添加到线程列表中

for t in threads:  # 遍历线程列表
    t.setDaemon(True)  # 将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
    t.start()  # 启动子线程
endtime = time.time();  # 记录程序结束时间
totaltime = endtime - starttime;  # 计算程序执行耗时
print("耗时：{0:.5f}秒".format(totaltime));  # 格式输出耗时
print('---------------------------')

# 以下为普通的单线程执行过程，不需解释
print("单线程：")
starttime = time.time();
task1();
task2();
endtime = time.time();
totaltime = endtime - starttime;
print("耗时：{0:.5f}秒".format(totaltime));
'''
'''
from tkinter import *
import time,threading,random,queue

exitFlag = 0
def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1
class MyThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      #print(self.name, self.counter, 5)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

app = Tk()
app.title("Circulation Open Lock")
app.geometry('600x200+400+100')     #默认窗体大小



#默认总循环次数
varSumCycleIndex = IntVar()
frameSumCycleIndex = Frame(app)
frameSumCycleIndex.pack(fill=X)
Label(frameSumCycleIndex, text = "总循环次数:", bg = "gray", fg = "white", width = 15).pack(side=LEFT)
inputSumCycleIndex = Entry(frameSumCycleIndex,textvariable = varSumCycleIndex)
varSumCycleIndex.set(10)
inputSumCycleIndex.pack(fill=X,side=LEFT,expand = 1)

#button
def xunhuanshuchu():
    sumi = int(inputSumCycleIndex.get())
    for i in range(1, sumi):
        print("+")
        time.sleep(1)
    print("I've just been clicked!")
def StartButtonClick():
    # Start new Threads
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")
b = Button(app, text = "开始!", width = 15, command = StartButtonClick)
b.pack(padx = 10, pady = 10)

#threading._start_new_thread()

app.mainloop()
'''
"""
import _thread, time
from tkinter import *
import threading,random,queue

app = Tk()
app.title("Circulation Open Lock")
app.geometry('600x200+400+100')     #默认窗体大小

# 为线程定义一个函数
def xunhuanshuchu(threadName):
    sumi = int(inputSumCycleIndex.get())
    for i in range(0, sumi):
        print("+ %s" % threadName)
        time.sleep(1)
    print("I've just been clicked! %s" % threadName)
#默认总循环次数
varSumCycleIndex = IntVar()
frameSumCycleIndex = Frame(app)
frameSumCycleIndex.pack(fill=X)
Label(frameSumCycleIndex, text = "总循环次数:", bg = "gray", fg = "white", width = 15).pack(side=LEFT)
inputSumCycleIndex = Entry(frameSumCycleIndex,textvariable = varSumCycleIndex)
varSumCycleIndex.set(2)
inputSumCycleIndex.pack(fill=X,side=LEFT,expand = 1)

#button
def StartButtonClick():
    # Start new Threads
    # 创建两个线程
    try:
        _thread.start_new_thread(xunhuanshuchu, ("Thread-1",))
        _thread.start_new_thread(xunhuanshuchu, ("Thread-2",))
        #_thread.start_new_thread(app.mainloop())
    except:
        print("Error: unable to start thread")
    xunhuanshuchu(1)
    print("Exiting Main Thread")

b = Button(app, text = "开始!", width = 15, command = StartButtonClick)
b.pack(padx = 10, pady = 10)
'''
# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while 1:
    pass
'''
app.mainloop()
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
import threading
import time
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))
# 创建两个线程
try:
    threading.start_new_thread(print_time, ("Thread-1", 2,))
    threading.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print
    "Error: unable to start thread"

while 1:
    pass
'''

import _thread
import time

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 15:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

        # 创建两个线程


try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while 1:
    pass