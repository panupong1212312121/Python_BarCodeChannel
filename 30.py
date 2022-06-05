food = 'bone'
animal = 'dog'

#print('My'+ ' '+ animal+' '+'eats'+' '+ food)


# {} = format field

print('My {1} eats {0}'.format('dog','bone'))
print('My {} eats {}'.format(animal,food))
print('My {animal} eats {food}'.format(animal ='dog',food ='bone'))

text = "My {} eats {}"
print(text.format("dog","bone"))

# add padding

animal = 'dog'

print("I have one {}".format(animal))
print("I have one {:10}".format(animal,animal))
print("I have one {:<10}".format(animal,animal))
print("I have one {:>10}".format(animal,animal))
print("I have one {:^10}".format(animal,animal))


# str.format(number)

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))