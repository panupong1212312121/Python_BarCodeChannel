
#Python tkinter button

from tkinter import *

count = 0
def click():
    global count
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file='click.png')
button = Button(window,
                text="Click me!",
                command=click,
                font=('Arial',30,'bold'),
                fg='white',
                bg='blue',
                activeforeground='white',
                activebackground='blue',
                image=photo,
                compound='bottom')

button.pack()
window.mainloop()