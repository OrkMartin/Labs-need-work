vvod = input('Введите М и Н через запятую - ')
l=list()
z=list(vvod)
u=''
z.append(',')
for i in z:
 if i==',':
  l.append(int(u))
  u=''
 else:
   u=u+i
m=l[0]
n=l[1]
print('',m,'=__',1,'*_',m)
if n!=0:
 if n<9:
  for a in range(2,n):
   if n<9:
    print(m*(a),'=__',a,'*_',m)
 elif n<99:
   for a in range(2,n+1):
    if a<10:
     print(m*(a),'=__',a,'*_',m)
    else:
     print(m*(a),'=_',a,'*_',m)
