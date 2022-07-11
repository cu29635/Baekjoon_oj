N = int(input())
jud = []
for i in range(N):
  x, y = map(int, input().split())
  jud.append((x,y))
jud.sort()
for i in jud:
  print(i[0], i[1])