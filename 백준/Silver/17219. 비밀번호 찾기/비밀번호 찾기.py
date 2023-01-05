n,m = map(int, input().split())
d = dict()
for i in range(n):
  a, b = map(str, input().split())
  d[a]=b
for i in range(m):
  k = input()
  print(d[k])