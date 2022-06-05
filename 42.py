


# # multi-level inheritance

class Grandparent:

    def alive(self):
        print('My Grand parent are alive')

class Parent(Grandparent):

    def home(self):
        print('My parent home is in Bangkok')

class Child(Parent):

    def play(self):
        print('I play games')


me = Child()

me.alive()