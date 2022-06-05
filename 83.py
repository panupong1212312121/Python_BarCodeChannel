
 # canvas

from tkinter import *

window =Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="black",width=5)
#canvas.create_line(0,500,500,0,fill="blue",width=5)
#canvas.create_rectangle(0,0,250,250,fill="red",width=5)
#canvas.create_polygon(250,0,500,500,0,500,fill="red",width=5)

canvas.create_arc(0,0,500,500,fill="red",width=5,start=180,extent=180)
canvas.create_arc(0,0,500,500,fill="red",width=5,start=0,extent=180)
canvas.create_oval(190,190,310,310,fill="white",width=5)




canvas.pack()


window.mainloop()