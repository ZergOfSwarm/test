from tkinter import *

#initialize the root window
root = Tk()


tk_button = Button(None, text = "1", fg="Blue")
tk_button.pack()

second_button = Button(None, text="2", fg="Red")
second_button.pack()

# Keep the window runing until user closes it
root.mainloop()
