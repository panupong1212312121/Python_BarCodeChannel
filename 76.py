#Python GUI filedialog save a file

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Administrator\\PycharmProjects\\pythonProject1\\Hallooo.txt",
                                    defaultextension='.txt',
                                    filetypes=[("Text file",".txt"),
                                               ("HTML file",".html"),
                                               ("All file",".*")])

    

    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text")
    file.write(filetext)


window =Tk()

button = Button(text="save",command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()