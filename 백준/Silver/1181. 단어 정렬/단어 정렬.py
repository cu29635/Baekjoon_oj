n = int(input())
a = list()
for _ in range(n):
  k = input()
  a.append(k)
a = list(set(a))
a.sort()
a.sort(key=lambda i:len(i))
for i in a:
  print(i)