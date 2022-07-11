N = int(input())
time = list(map(int, input().split()))
time.sort()

cnt = 0
prev = 0
for t in time:
  prev = prev + t
  cnt = cnt + prev
print(cnt)