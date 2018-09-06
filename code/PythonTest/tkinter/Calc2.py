from tkinter import *
import Pmw

class SLabel(Frame):
    """SLabel defines a 2-sided label within a Frame. The left hand label has blue letters the right has white letters"""
    def __init__(self, master, leftl, rightl):
        Frame.__init__(self, master, bg='gray40')
        self.pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self, text=leftl, fg='steelbluel', font=("arial", 6, "bold"), width=5, bg='gray40').pack(side=LEFT, expand=YES, fill=BOTH)
        Label(self,)