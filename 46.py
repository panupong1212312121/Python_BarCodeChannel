
# #abstract classes 
# 1. class ลูกที่สืบทอดจาก class แม่ บังคับว่าต้องดำเนินการทุก function ใน class แม่ (สำหรับกันลืม)
# 2. บังคับให้ dev ห้ามสร้าง object จาก class ที่ใน method มี @abstractmethod (สำหรับไว้เป็น template เฉย ๆ)

from abc import ABC, abstractmethod

class idea(ABC):

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def read(self):
        pass

class Math(idea):

    def write(self):
        print('I am writing Math')

    def read(self):
        print('I am reading Math')


class English(idea):

    def write(self):
        print('I am writing English')

    def read(self):
        print('I am reading English')




class1 = Math()
class2 = English()


class1.write()
class2.write()