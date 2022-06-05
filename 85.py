#python drag and drop widget

from tkinter import *

def startclick(event):
    widget = event.widget
    widget.startclickX = event.x
    widget.startclickY = event.y

def finalmotion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startclickX + event.x
    y = widget.winfo_y() - widget.startclickY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)



label.bind("<Button-1>",startclick)
label.bind("<B1-Motion>",finalmotion)




window.mainloop()