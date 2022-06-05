

# # variable scope

fruit = 'orange'

def local_fruit():
    fruit = 'durian'
    print(fruit)


local_fruit()
print(fruit)