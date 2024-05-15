

# Python multithreading
# thread = เครื่องจักร/คนงาน
# cpu bound = ทำงานภายใน/CPU intensive
# io bound =ทำงานภายนอก/user input, web scraping

import threading
import time

def eat_breakfast():
    time.sleep(1)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(2)
    print("You drink coffee")
def study():
    time.sleep(3)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast,args=())
x.start()
y = threading.Thread(target=drink_coffee,args=())
y.start()
z = threading.Thread(target=study,args=())
z.start()

# x.join()
# y.join()
# z.join()

print(threading.active_count())
print(threading.enumerate())