#Python checkbox

from tkinter import *

def display():
    if(x.get()==1):
        print("You are agree")
    else:
        print("You don't agree")



window = Tk()

Photo = PhotoImage(file='cat.png')
x = IntVar()

checkbox_button = Checkbutton(window,
                              text="I agree to something",
                              font=('Arial',25),
                              fg='#00FF00',
                              bg='black',
                              activeforeground='#00FF00',
                              activebackground='black',
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display,
                              image=Photo,
                              compound='left')

checkbox_button.pack()

window.mainloop()