a = int(input("Длина: "))
b = int(input("Ширина: "))
list=[]

st = '*'
poi = '.'

row = a * poi
row = st + row[1:-1] + st
row2 = a * st

list.append(row2)
for i in range(b):
    list.append(row)
list.append(row2)
print(list)

