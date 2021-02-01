from tkinter import *
root = Tk()
root.title("Simple calculator")
e = Entry(root, width=40, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add():
    return


button_1 = Button(root, text="1", padx=30, pady=20, command=button_add)
button_2 = Button(root, text="2", padx=30, pady=20, command=button_add)
button_3 = Button(root, text="3", padx=30, pady=20, command=button_add)

button_4 = Button(root, text="4", padx=30, pady=20, command=button_add)
button_5 = Button(root, text="5", padx=30, pady=20, command=button_add)
button_6 = Button(root, text="6", padx=30, pady=20, command=button_add)

button_7 = Button(root, text="7", padx=30, pady=20, command=button_add)
button_8 = Button(root, text="8", padx=30, pady=20, command=button_add)
button_9 = Button(root, text="9", padx=30, pady=20, command=button_add)

button_0 = Button(root, text="0", padx=30, pady=20, command=button_add)
button_add = Button(root, text="+", padx=30, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=87, pady=20, command=button_add)

button_clear = Button(root, text="clr", padx=84, pady=20, command=button_add)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)


root.mainloop()
