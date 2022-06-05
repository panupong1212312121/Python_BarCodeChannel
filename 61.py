
import time

print(time.ctime(time.time()))
print(time.localtime())
print(time.strftime("%B %d %Y %H:%M:%S",time.gmtime()))

#time.strptime(time_string, fomat)
time_string = "1 January 2020"
print(time.strptime(time_string, "%d %B %Y"))
print(time.strftime("%B %d %Y %H:%M:%S",time.strptime(time_string, "%d %B %Y")))

#time.asctime(time_tuple)
(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2022, 1, 1, 10, 20, 0, 0, 0, 0)
print(time.asctime(time_tuple))
print(time.mktime(time_tuple))