import math

result = [0 for i in range(10000001)]
result[1] = 1
for i in range(2,10000001):
  if result[i]==0 :
    for j in range(i*2,10000001,i):
      result[j]=1
n, m = map(int, input().split())
cnt = 0
for i in range(2,int(math.sqrt(m))+1,1):
  if result[i] == 0:
    k = i
    while(1):
      k = k*i
      if k<=m and k>=n:
        cnt += 1
      if k>m : break
print(cnt)