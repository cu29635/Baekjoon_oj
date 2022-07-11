import sys
N, C = map(int, input().split())
home = [int(sys.stdin.readline()) for _ in range(N)]

home.sort()
start = 1
end = max(home) - min(home)
while start<=end:
  mid = (start+end)//2
  home_pre = home[0]
  cnt = 1
  for i in range(1,N):
    if(home[i]-home_pre>=mid):
      cnt += 1
      home_pre = home[i]
  if cnt>=C:
    ans = mid
    start = mid + 1
  else:
    end = mid -1
print(ans) 