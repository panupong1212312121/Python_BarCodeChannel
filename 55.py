# map(function,iterable)
# filter(function return True,iterable)


store_dollar = [("shirt",20.00),
                ("pants",25.00),
                ("jacket",50.00),
                ("socks",10.00)]


def to_baht(data):
    return (data[0],round(data[1]*32))

store_baht = map(to_baht,store_dollar)

def to_baht2(data):
    return (data[1]<=1000)

store_baht2 = filter(to_baht2,store_baht)

for i in store_baht2:
    print(i)