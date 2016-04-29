
p = input('Введите порядковый номер требуемого числа Фибоначчи ')
a=1
a2=0
for i in range(int(p)):
 a=(a+a2)%10
 a2=(a-a2)%10

print(a)
input()
