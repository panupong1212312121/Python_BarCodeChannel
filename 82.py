#Python progress bar

from tkinter import *
from tkinter.ttk import *
import time

def start():
    task = 100
    x = 0
    speed = 1
    while(x<task):
        time.sleep(0.05)
        bar['value']+=(speed/task)*100
        x += speed
        percent.set(str(int((x/task)*100))+"%")
        text.set(str(x)+"/"+str(task)+"task completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)


percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()


window.mainloop()