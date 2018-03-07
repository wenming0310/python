#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import threading, time, serial
import serial.tools.list_ports

#获取当前存在的串口

class serialcontrol(object):
    def __init__(master=None):
        time.sleep(1)
        plist = serial.tools.list_ports.comports()
        if len(plist) <= 0:
            print("The Serial port can't find!")
        else:
            [print(plist[item]) for item in range(len(plist))]
            #for i in range(len(plist)):
            #    #list[x = list(plist[i])
            #    print(plist[i])
            #plist_0 = list(plist[0])
            #serialName = plist_0[0]
            #serialFd = serial.Serial(serialName, 9600, timeout=60)
            #print("check which port was really used >", serialFd.name)




if __name__=="__main__":
    serialcontrol.__init__()