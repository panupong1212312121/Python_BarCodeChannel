#Python animation multiple object
import time
from tkinter import *
from ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"red")
tennis_ball = Ball(canvas,0,0,50,3,2,"green")

while True:
    volley_ball.move()
    tennis_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()


-------------------------------------------------------------------------------------------------

class Ball:
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)

        if(coordinates[0]<0 or coordinates[2] >= self.canvas.winfo_width()):
            self.xVelocity = -self.xVelocity

        if (coordinates[1] < 0 or coordinates[3] >= self.canvas.winfo_height()):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)