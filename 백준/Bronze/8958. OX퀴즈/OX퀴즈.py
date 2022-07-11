n = int(input())
for _ in range(n):
  arr = input()
  cnt = 0
  score = 0
  for j in range(len(arr)):
    if(arr[j]=='O'):
      score +=1
      cnt = cnt + score
    else :
      score = 0
  print(cnt)