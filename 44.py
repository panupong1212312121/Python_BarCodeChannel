


# # method chaining

class Car:

    def turn_on(self):
        print('you start the engine')
        return self

    def drive(self):
        print('you are driving')
        return self

    def brake(self):
        print('you are braking')
        return self

    def turn_off(self):
        print('you are turning off')
        return self


car = Car()

car.turn_on().drive().brake().turn_off()