# #duck typing

class Duck:

    def walk(self):
        print('The duck is walking')

    def talk(self):
        print('The duck is qwuacking')

class Person():

    def catch(self,animals):
        animals.walk()
        animals.talk()


duck_1 = Duck()
person_1 = Person()

person_1.catch(duck_1)