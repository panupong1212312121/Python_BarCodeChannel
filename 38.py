
#os.remove(path)     ลบไฟล์
#os.rmdir(path)      ลบโฟลเดอร์ว่าง
#shutil.rmtree(path) ลบโฟลเดอร์ที่มีไฟล์


import os
import shutil


source = 'folder'


try:


    #os.remove(source)
    #os.rmdir(source)
    shutil.rmtree(source)
    
except FileNotFoundError:
    print('That file was not found')


except OSError:
    print('you can not using this function delete this folder')