x=input()
l=list(x)
i2=1
mx=max(l)
for i in l:
  if(int(i)!=int(mx)):
   if (int(i)>int(i2)):
    mx2=int(i)
   else: mx2=int(i2)
  i2=int(i)
print(mx2)
print()
