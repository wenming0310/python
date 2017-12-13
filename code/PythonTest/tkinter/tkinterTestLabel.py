from tkinter import *

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

num_good = IntVar()
num_good.set(0)

l = Label(app, text = 'When you are ready, click on the buttons!', height = 3)
l.pack()

ll = Label(app, textvariable = num_good)
ll.pack(side = 'left')

num_good.set(100)

app.mainloop()