# #dictionary =  {key:value}

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals.keys())
#print(capitals.values())
print(capitals.items())
#print(capitals.get('Thailand'))

capitals.update({'Thailand':'Bangkok'})
capitals.update({'USA':'New york'})
capitals.pop('Russia')
capitals.clear()

for key,value in capitals.items():
    print(key,value)