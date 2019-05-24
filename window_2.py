from tkinter import *
 
def mainWindow():
    root = Tk()
    root.geometry('300x300')
    root.title('Основное окно')
 
    val = StringVar()
 
    def new_window(event):
        root.destroy()
        secondWindow(val)
 
    lab = Label(root, text='Нажми')
    but = Button(root, text='Ok')
    but.bind('<Button->', new_window)
     
    entry = Entry(root, textvariable=val)
     
    lab.pack()
    but.pack()
    entry.pack()
     
    root.mainloop()
    
def secondWindow(val_):
    window = Tk()
    window.geometry('400x400')
    window.title('Второе окно')
    val = StringVar()
    val.set(val_.get())
    entry = Entry(window, textvariable=val)
    entry.pack()
 
    window.mainloop()
    
if __name__ == '__main__':
    mainWindow()
