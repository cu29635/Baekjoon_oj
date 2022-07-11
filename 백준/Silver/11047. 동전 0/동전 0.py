N, K = map(int, input().split())
cnt = 0
coin = []
for _ in range(N):
  c = int(input())
  coin.append(c)
coin.sort(reverse=True)
for c in coin:
  if(K>=c):
    cnt = cnt + K//c
    K = K - c*(K//c)
print(cnt)