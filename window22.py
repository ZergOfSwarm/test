from tkinter import *
from tkinter import messagebox # Зачем нужно импортировать если мы выше импортировали все?

def clicked():
    #messagebox.showinfo('Вопрос', 'Вы точно хотите знать ответ?')
    answer = messagebox.askyesno(title="Вопрос", message="Перенести данные?")
    if answer == True:
        #s = entry.get()
        #entry.delete(0, END)
        #label['text'] = s


root = Tk()
root.title("Вы уверены?")
root.geometry("400x300+300+250")
btn = Button(root, text='Не нажимать!', command=clicked)
#btn.grid(column=2, row=2)
btn.place(relx=.5, rely=.5, anchor="center") # выставит строго по центру кнопку!

#messagebox.showinfo('Заголовок', 'Текст')


root.mainloop()
