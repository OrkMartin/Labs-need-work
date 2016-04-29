text=input()
len(text)
for i in range(0,len(text)-1):
 if abs(int(len(text))%int(i))==0:
  k=i

print(k)