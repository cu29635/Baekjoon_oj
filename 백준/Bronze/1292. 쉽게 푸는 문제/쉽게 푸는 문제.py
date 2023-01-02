x,y = map(int, input().split())
s = 0
cnt = 0
i = 0
while(True):
  i += 1
  for j in range(i):
    cnt += 1
    if(cnt>=x and cnt<=y):
      s = s + i

  if(cnt>y) : break
print(s)