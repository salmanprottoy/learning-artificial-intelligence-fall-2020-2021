# move an Image on the canvas with tkinter

import tkinter as tk
import numpy as np
from scipy import ndimage
from PIL import Image

# Create the window with the Tk class
root = tk.Tk()

# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=700, height=500, bg="Royal Blue")
canvas.pack()  # this makes it visible

# Loads and create image (put the image in the folder)
img = tk.PhotoImage(file="XOsf.gif")
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)


def move(event):
    if event.char == 'a' or event.keysym == 'Left':
        canvas.move(image, -10, 0)
    elif event.char == 'd' or event.keysym == 'Right':
        canvas.move(image, 10, 0)
    elif event.char == 'w' or event.keysym == 'Up':
        canvas.move(image, 0, -10)
    elif event.char == 's' or event.keysym == 'Down':
        canvas.move(image, 0, 10)


for i in range(1, 14):
    x = 0 + 50 * i
    y = 25
    c = canvas.create_oval(x, y, x + 10, y + 10, fill="White")


for i in range(1, 14):
    x = 0 + 50 * i
    y = 75
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range( 1, 14):
    x = 0 + 50 * i
    y = 125
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 175
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 225
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 275
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 325
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 375
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 425
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")

for i in range(1, 14):
    x = 0 + 50 * i
    y = 475
    canvas.create_oval(x, y, x + 10, y + 10, fill="White")


canvas.create_rectangle(58, 86, 137, 104, fill="grey")
canvas.create_rectangle(58, 105, 73, 186, fill="grey")
canvas.create_rectangle(63, 370, 148, 390, fill="grey")
canvas.create_rectangle(63, 370, 78, 297, fill="grey")

# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)

# this creates the loop that makes the window stay 'active'
root.mainloop()
