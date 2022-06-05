phone_number = '123-456-789'

for i in phone_number:
    if i == '-':
        break
    print(i,end='')

phone_number = '123-456-789'

for i in phone_number:
    if i == '-':
        continue
    print(i,end='')

phone_number = '123-456-789'

for i in phone_number:
    if i == '-':
        pass
    else:
        print(i,end='')