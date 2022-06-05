
# #python object oriented programming

class Car:

    def __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('This '+self.brand+' is driving')

    def stop(self):
        print('This '+self.brand+' is stopped')


car_1 = Car('Isuzu','V-cross','2021','blue')
car_2 = Car('MG','Extender','2021','white')


car_1.drive()
print(car_1.color)

car_2.drive()
car_2.stop()
print(car_2.brand)