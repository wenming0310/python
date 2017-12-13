'''
my_small_field = Entry(app)
my_large_field = Text(app)
my_entry_field.get()
my_entry_fild.insert(0, "banana")
my_entry_field.delete(0, END)
my_large_field.get("1.0", END)
my_large_field.delete("1.0", END)
my_large_field.insert("1.0", "Some text")
'''

from tkinter import *

def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0",END))
    depot.delete(0,END)
    description.delete(0,END)
    address.delete("1.0",END)

app = Tk()
app.title("Head-Ex Deliveries")
#app.geometry('300x100+200+100')
Label(app, text = "Depot:").pack()
depot = Entry(app)
depot.pack()
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()
Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()