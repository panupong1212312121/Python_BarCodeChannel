#Python GUI filedialog

from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Administrator\\PycharmProjects\\pythonProject1\\My file.txt",
                                          title="Open file",
                                          filetypes=(("text files","*.txt"),("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())

window =Tk()

button = Button(text="Open",command=openfile)
button.pack()

window.mainloop()