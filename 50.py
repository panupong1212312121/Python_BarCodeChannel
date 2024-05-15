# #python function variable


def hello():
    print('world')

print(hello)

hi = hello

hi() #print process

print(hi) #print address


say = print
say('this is my world')
print('this is my world')