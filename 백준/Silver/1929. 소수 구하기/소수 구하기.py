M, N = map(int,input().split())

result = [True] * (N+1)
cnt = 0
result[1] = False
for i in range(2,N+1):
  if result[i]:
    for j in range(i+i,N+1,i):
      if(result[j]!=False):
        result[j] = False

for i in range(M,N+1):
  if result[i]:
    print(i)
