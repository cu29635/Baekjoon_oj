N = int(input())
jud = []
for i in range(N):
  age, name = map(str, input().split())
  jud.append((int(age),name))
jud.sort(key=lambda jud:jud[0])
for i in jud:
  print(i[0], i[1])