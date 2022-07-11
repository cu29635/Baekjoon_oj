N, K = map(int,input().split())

result = [True] * (N+1)
cnt = 0
for i in range(2,N+1):
  if result[i]:
    for j in range(i,N+1,i):
      if(result[j]!=False):
        result[j] = False
        cnt += 1
        if(cnt==K) :
          print(j)