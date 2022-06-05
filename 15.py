
name = 'ABC_DEF'

fist_name = name[0:3]
last_name = name[4:7]
step_name = name[::-1]


print(fist_name)
print(last_name)
print(step_name)

place1 ='abc_bangkok_def'
place2 ='ghi_phuket_jkl'

slice = slice(4,-4,2)

print(place1[slice])
print(place2[slice])