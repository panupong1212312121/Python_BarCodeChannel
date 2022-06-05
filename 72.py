#messagebox

from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="Info",message="You are a person")
    #messagebox.showwarning(title="Warning", message="Something went wrong")
    #messagebox.showerror(title="Error", message="You have  A VIRUS!!")

    #if messagebox.askokcancel(title="askokcancel", message="Are you sure to do this?"):
        #print("You did a thing")
    #else:
        #print("You canceled a thing")


    #if messagebox.askretrycancel(title="retrycancel", message="Do you want to retry again?"):
        #print("You retried a thing")
    #else:
        #print("You canceled a thing")


    #if messagebox.askyesno(title="askyesno", message="Do you like swimming?"):
        #print("Yes I do")
    #else:
        #print("No I don't")

    #answer=messagebox.askquestion(title="askyesno", message="Do you like swimming?")

    #if(answer=='yes'):
        #print("Yes I do")
    #else:
        #print("No I don't")

    #print(messagebox.askyesnocancel(title="askyesno", message="Do you like swimming?"))

    answer = messagebox.askyesnocancel(title="askyesno", message="Do you like swimming?")

    if (answer == True):
        print("Yes I do")
    elif(answer == False):
        print("No I don't")
    else:
        print("You canceled it")



window = Tk()

button = Button(window,command=click,text="click me")
button.pack()

window.mainloop()