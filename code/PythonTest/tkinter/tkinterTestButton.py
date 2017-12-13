'''
from tkinter import *

app = Tk()
app.title("Your tkinter application")
app.geometry('450x200+200+200')     #'450x200+200+200' 450*200主题
#app.wm_geometry()
bl = Button(app, text = "Click me!", width = 10)
bl.pack(padx = 10, pady = 10)

top = Button(app, text = "Top", width = 10)
top.pack(side = 'top')
bottom = Button(app, text = "Bottom", width = 10)
bottom.pack(side = 'bottom')
left = Button(app, text = "Left", width = 10)
left.pack(side = 'left')
right = Button(app, text = "Right", width = 10)
right.pack(side = 'right')

app.mainloop()
'''
'''
from tkinter import *

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

b1 = Button(app, text = "Correct!", width = 10)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop()
'''
from tkinter import *

app = Tk()
app.title("Click on me")
app.geometry('300x100+200+100')

def button_click():
    print("I've just been clicked!")

b = Button(app, text = "Click on me!", width = 15, command = button_click)
b.pack(padx = 10, pady = 10)

app.mainloop()