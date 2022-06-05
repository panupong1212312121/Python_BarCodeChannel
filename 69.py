 # radio button

from tkinter import *

food = ["pizza","coffee","french fries"]

def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered Coffee")
    elif(x.get()==2):
        print("You ordered French fries")
    else:
        print("Please order")

window =Tk()

pizzaimage= PhotoImage(file='pizza.png')
coffeeimage = PhotoImage(file='coffee-cup.png')
frenchfries=PhotoImage(file='fried-potatoes.png')
foodimages = [pizzaimage,coffeeimage,frenchfries]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font = ("Impact",40),
                              image = foodimages[index],
                              compound = 'left',
                              command = order,
                              indicatoron= 0,
                              width=350

                            )
    radiobutton.pack(anchor=W)

window.mainloop()