from tkinter import *


top = Tk()
e = Entry(top, width=50, bg="gray")
e.pack()


def hellocallback():
    hello = "hello, " + e.get()
    label = Label(top, text=hello)
    label.pack()


B = Button(top, text="click here", command=hellocallback())

B.pack()
top.mainloop()
