# -*-coding: UTF-8 -*-
__author__ = 'zwm'

import os, getpass, time
from tkinter import *   #导入tkinter的所有类不需要加前缀
#import tkinter as tk



def main():
    top = Tk()
    # 进入消息循环
    top.mainloop()


if __name__ == '__main__':
    #python文件后缀为".py"。 其中分两类：一类是直接执行， 另一类是作为模块被调用(import ***.py).
    #__name__ 作为模块的内置属性，即".py"文件的调用方式。如果等于“__main__"就直接执行本文件， 如果是别的就是作为模块被调用
    main()