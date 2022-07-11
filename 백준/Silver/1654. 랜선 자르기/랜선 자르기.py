K, N = map(int, input().split())
lan = []
for _ in range(K):
  cm = int(input())
  lan.append(cm)

s = 1
e = max(lan)
lan.sort(reverse=True)
while s<=e:
  cnt = 0
  mid = (s+e)//2
  for sun in lan:
    cnt += sun//mid
  if N<=cnt:
    s  = mid + 1
  else :
    e = mid -1

print(e)