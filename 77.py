#Python Menu Bar

from tkinter import *

def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved")
def Cut():
    print("You cut some text")
def Copy():
    print("You copied some text")
def Paste():
    print("You pasted some text")


window = Tk()

cutImage = PhotoImage(file="cut.png")
copyImage = PhotoImage(file="copy-two-paper-sheets-interface-symbol.png")
pasteImage = PhotoImage(file="paste.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Free Ink",15))
menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Exit")


editMenu = Menu(menubar,tearoff=0,font=("Free Ink",15))
menubar.add_cascade(label="Edit",menu=editMenu)

editMenu.add_command(label="Cut",command=Cut,image=cutImage,compound='left')
editMenu.add_command(label="Copy",command=Copy,image=copyImage,compound='left')
editMenu.add_command(label="Paste",command=Paste,image=pasteImage,compound='left')



window.mainloop()