


# # python super function

class Car:

    def __init__(self,brand,buy,now,color):
        self.brand = brand
        self.buy = buy
        self.now = now
        self.color = color


class Van(Car):

    def __init__(self, brand, buy, now, color,paid):
        super().__init__(brand,buy,now,color)
        self.paid = paid


    def pay(self):
        return (self.now-self.buy)*self.paid



Van_1 = Van('Isuzu',2010,2021,'blue',50000)

print(Van_1.pay())