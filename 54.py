


# # map(function,iterable)

store_dollar = [("shirt",20.00),
                ("pants",25.00),
                ("jacket",50.00),
                ("socks",10.00)]

def to_baht(data):
    return (data[0],round(data[1]*32))

store_baht = map(to_baht,store_dollar)

for i in store_baht:
    print(i)