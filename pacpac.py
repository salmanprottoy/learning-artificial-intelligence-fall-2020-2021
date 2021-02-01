import tkinter as tk


root = tk.Tk()
root.grid_location(900, 900)
canvas = tk.Canvas(root, width=820, height=600, bg="RoyalBlue")
canvas.pack()
# root.grid_location(900, 900)

oval = canvas.create_oval(100, 100, 150, 150, fill="yellow")

# img = tk.PhotoImage(file="pac.ppm")
# canvas.create_image(20, 20, anchor='NW', image=img)

def move(event):
    if event.char == 'a' or event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    elif event.char == 'd' or event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    elif event.char == 'w' or event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.char == 's' or event.keysym == 'Down':
        canvas.move(oval, 0, 10)


root.bind("<Key>", move)
root.mainloop()