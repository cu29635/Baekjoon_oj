N = int(input())
n = 1001
qq  = list(map(int,input().split()))
result = [False,False] + [True] * (n)

for i in range(2,n):
  if result[i]:
    for j in range(i+i,n,i):
      result[j] = False
cnt = 0
for x in qq:
  if result[x]:
    cnt += 1
print(cnt)