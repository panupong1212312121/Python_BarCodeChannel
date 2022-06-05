
# zip(*iterables)


usernames = ["banana", "apple", "melon"]
passwords = ("1234", "54321", "888999")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

users = list(zip(usernames,passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+" : "+value)

# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)