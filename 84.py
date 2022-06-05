#Python keyboard event

from tkinter import *

def Hello(event):
    print("Hello:"+ event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",Hello)

label = Label(window,font=("Arial",50))
label.pack()

window.mainloop()