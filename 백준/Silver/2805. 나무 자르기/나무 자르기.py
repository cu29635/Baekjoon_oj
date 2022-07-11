N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort(reverse=True)
cnt=0
s = 0
e = tree[0]
while s<=e :
  mid = (s+e)//2
  cnt = 0
  for t in tree:
    if t>mid:
      cnt += t - mid
  if M <=cnt :
    s = mid + 1
  else:
    e = mid -1
print(e)