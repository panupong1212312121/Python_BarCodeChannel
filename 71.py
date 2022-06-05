
# listbox

def submit():
    print("You have ordered")
    #print(listbox.get(listbox.curselection()))
    food = []

    for i in listbox.curselection():
        food.insert(i,listbox.get(i))

    for i in food:
        print(i)


def delete():
    #listbox.delete(listbox.curselection())
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())


def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

from tkinter import *

window =Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=15,
                  selectmode=MULTIPLE)

listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"galic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frameBox = Frame(window)
frameBox.pack()

submitButton = Button(frameBox,
                      text="submit",
                      command=submit)
submitButton.pack(side=LEFT)

deleteButton = Button(frameBox,
                      text="delete",
                      command=delete)
deleteButton.pack(side=LEFT)

addButton = Button(frameBox,
                   text="add",
                   command=add)
addButton.pack(side=LEFT)



window.mainloop()