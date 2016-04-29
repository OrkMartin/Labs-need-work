#a=input('Введите веса ступеней через запятую - ')
#rstep=input('Введите ширину шага - ')
a='5,3,6,1,1,2,3,4,7,5,5,7,1,1,4,6,3,4,7,4,2'
rstep=int('4')
l=list()
z=list(a)
u=''
z.append(',')
for i in z:
 if i==',':
  l.append(int(u))
  u=''
 else:
   u=u+i
z=len(l)-1
rich=1
weight=0
while z>=rstep:
  minw=int('9999')
  for i in range(rstep):
   if minw>=l[z-i]:
    minw=l[z-i]
    minn=z-i
    print(minn,minw)
  z=minn-1
  weight=weight+minw
  print(weight)
print(weight)
input()
