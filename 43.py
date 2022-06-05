


# # multi-level inheritance overriding

class Grandparent:

    def alive(self):
        print('My Grand parent are alive')

class Parent:

    def home(self):
        print('My parent home is in Bangkok')

class Child(Parent,Grandparent):

    def home(self):
        print('I live in Chiang mai')


me = Child()

me.home()