# # sort() method   = lists
# sort() function = iterables


Labbage, [12/18/2021 2:02 PM]
students = ["Leo","Max","Jack","Lena","Molly"]
students.sort()
for i  in students:
    print(i)


students = (("Leo", "F", 24),
            ("Max", "A", 23),
            ("Jack","D", 25),
            ("Lena","B", 21),
            ("Molly","C", 22))

def column(index):
    return index[2]

students2 = sorted(students,key=column,reverse=True)

for i in students2:
    print(i)