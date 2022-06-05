import os

path = "C:\\Users\\Administrator\\OneDrive\\เอกสาร\\New folder"

if os.path.exists(path):
    print("that location is exists")
    if os.path.isfile(path):
        print('that is file')
    elif os.path.isdir(path):
        print('that is folder')

else:
    print("that location doesn't exists")