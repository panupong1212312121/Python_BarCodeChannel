# #objects as arguments

class Car:


    color = None
    year = None



def attributes(car,color,year):
    car.color = color
    car.year = year


car_1 = Car()
attributes(car_1,'blue',2021)

print(car_1.year)