# nested loops

rows = int(input('How many rows?: '))
columns = int(input('How many columns?: '))
symbol = input('Enter a symbol to use: ')

for a in range(rows):
    for b in range(columns):
        print(symbol,end='')

    print('')