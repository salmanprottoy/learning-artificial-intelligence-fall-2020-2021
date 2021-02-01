import tkinter as tk

from PIL import Image

can = tk.Canvas(width=800, height=800, bg="Royal Blue")
can.pack()
img = tk.PhotoImage(file="XOsf.gif")
image = can.create_image(10, 10, anchor=tk.NW, image=img)


def motion():
    if m == 1:
        can.move(image, 0, -10)
    elif m == 3:
        can.move(image, 0, 10)
    elif m == 0:
        can.move(image, 10, 0)
    else:
        can.move(image, - 10, 0)
    can.after(50, motion)


def arrows(event):
    global m
    if event.keysym == 'Up':
        m = 1
    elif event.keysym == 'Down':
        m = 3
    elif event.keysym == 'Right':
        m = 0
    else:
        m = 2

#root = can.create_oval(100, 100, 150, 150, fill="yellow")

m = 0

motion()
can.bind('<Button-1>', motion)
can.bind_all('<Key>', arrows)

can.mainloop()