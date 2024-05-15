

#daemon thread = ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    count = 0
    while True:
        print()
        print()
        time.sleep(1)
        count += 1
        print("logged in for:",count,"seconds")


x = threading.Thread(target=timer,daemon=True) # กำหนด daemon=True เพื่อให้เวลา user input something เสร็จแล้ว ให้ threading timer หยุด 
x.start()

answer=input("Do you want to exit")