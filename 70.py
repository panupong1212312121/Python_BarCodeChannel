#GUI scale

from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degree C")

window = Tk()

hotimage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotimage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              font=('Arial',20),
              tickinterval= 10,
              resolution=5,
              troughcolor='#69EAFF',
              fg= '#FF1C00',
              bg='#111111')

scale.set((scale['from']-scale['to'])/2)
scale.pack()

coldimage = PhotoImage(file='snowflake.png')
coldLabel = Label(image=coldimage)
coldLabel.pack()

button = Button(window,
                text="submit",
                command=submit)

button.pack()

window.mainloop()