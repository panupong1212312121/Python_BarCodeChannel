

from tkinter import *

window = Tk()

photo = PhotoImage(file='cat.png')
label = Label(window,
              text='Hello Cat',
              font=('Arial',30,'bold'),
              fg='red',
              bg='black',
              relief=RAISED,
              bd=20,
              padx=30,
              pady=30,
              image=photo,
              compound ='bottom')

label.pack()
window.mainloop()