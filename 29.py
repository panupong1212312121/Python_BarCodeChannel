
# **kwargs = เก็บ value ทั้งหมดให้อยู่ในรูป dict
def address(**kwargs):
    #print('My home is '+ kwargs['number'] +' ' + kwargs['city']+ ' ' +kwargs['country'])

    for key,value in kwargs.items():
        print(value,end=' ')

address(city='bangkok',number='99/123',country='Thailand')