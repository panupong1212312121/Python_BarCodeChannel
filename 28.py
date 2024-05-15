

# # *args : เก็บ value ทั้งหมดให้อยู่ในรูป tuple

def add(*result): 
    sum = 0
    result = list(result)
    result[0] = 10

    for i in result:
        sum += i
    return sum

print(add(5,10,15,20))