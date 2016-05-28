print('Введите строку:')
s = input()
n = len(s)
i = 2
k = 0

while i < n:
 if n % i == 0:
  if n / i == s.count(s[:i]):
   if s.count(s[:i]) > k:
    k = s.count(s[:i])
    t = i
 i += 1
print('k=', k, '\n t=', s[:t] )


input()
