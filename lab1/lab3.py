class point:
 def __init__(self,x,y):
   self.x=x
   self.y=y

x=input()
l=list()
z=list(x)
u=''
z.append(',')
for i in z:
 if i==',':
  l.append(u)
  u=''
 else:
   u=u+i
 '''
for i in range(0,l.count(',')):
 l.remove(',')
 '''
print(l)
a=list()
i=0
while i <int(len(l)):
 a.append(point(l[i],l[i+1]))
 i=i+2
for i in a:
 print(i.x,i.y)

slope=(float(a[0].y)-float(a[1].y))/(float(a[0].x)-float(a[1].x))
slope2=(float(a[2].y)-float(a[3].y))/(float(a[2].x)-float(a[3].x))
if slope==slope2:
 print('YES')
else:
 print('NO')
 
print()
