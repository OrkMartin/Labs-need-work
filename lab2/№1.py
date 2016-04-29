text=open('Text.txt', 'r')
wtext=text.read()
u=''
wordmas=list()
wtext=wtext+' '
for i in wtext:
 if i==' ':
  wordmas.append(u)
  u=''
 else:
   u=u+i
maxw=''
maxi=0
for i in wordmas:
 if maxi<wordmas.count(i):
  maxw=i
  maxi=wordmas.count(i)
print(maxw)
'''
 for z in range(0,wordmas.count(i)):
  wordmas.remove(i)
'''
input()
